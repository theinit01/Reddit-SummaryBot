import praw
import re
from bs4 import BeautifulSoup
import requests
from llmsummary import summarize
import os
from dotenv import load_dotenv
from pathlib import Path
import json


# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

username = os.environ.get("REDDIT_USERNAME")
password = os.environ.get("REDDIT_PASSWORD")
client_id = os.environ.get("REDDIT_CLIENT_ID")
client_secret = os.environ.get("REDDIT_CLIENT_SECRET")

def getTextFromURL(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return text

def load_posted_summaries():
    try:
        with open('posted_summaries.json', 'r') as file:
            return set(json.load(file))
    except FileNotFoundError as e:
        print(e)
        return set()

def save_posted_summaries(posted_summaries):
    with open('posted_summaries.json', 'w') as file:
        json.dump(list(posted_summaries), file)

reddit_instance  = praw.Reddit(client_id=client_id, client_secret=client_secret, username=username, password=password, user_agent="Sumarizer-Bot")

subreddit = reddit_instance.subreddit("india")
top_posts = subreddit.rising(limit=7)

posted_summaries = load_posted_summaries()

for post in top_posts:
    if not post.is_self:
        if post.id in posted_summaries:
            continue
        
        url = post.url
        article = getTextFromURL(url)
        summary = summarize(article)
        
        if "This is not an article." not in summary:
            post.reply("Here is a summary of the article: \n\n" + summary)
            print(f"Posted summary for post: {post.title}")
            posted_summaries.add(post.id)

save_posted_summaries(posted_summaries)