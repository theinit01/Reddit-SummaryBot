import textwrap

import google.generativeai as genai
from IPython.display import Markdown
import os
from dotenv import load_dotenv
from pathlib import Path


# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

prompt = f"""You are a news summarizer. Sumarrize the news article given in backticks. Keep it short and concise but keep all the relevant and required information. If it has any quotaions, keep them as it is. If you think it is not an article, Please say the following line only 'This is not an article.'"""


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def summarize(article):
    model = genai.GenerativeModel('gemini-pro')
    new_prompt = prompt + f"\n\n```\n{article}\n```"
    response = model.generate_content(new_prompt)
    return response.text