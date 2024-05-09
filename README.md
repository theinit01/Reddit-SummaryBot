
# Article Summarizer Bot

Article Summarizer Bot is a Reddit bot designed to automatically summarize news articles and post the summaries as comments on related posts in a subreddit.

## Introduction

This bot was created to assist users in staying informed about news articles posted on a specific subreddit. It scans the content of news articles linked in the subreddit posts, generates concise summaries using Goggle's Gemini, and posts these summaries as comments on the original posts.

## Features

- Automatically scans 'rising' posts in a subreddit for news articles
- Generates summaries of linked news articles
- Posts summaries as comments on relevant posts

## Getting Started

To use the Article Summarizer Bot, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/article-summarizer-bot.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Reddit  and Google Gemini API credentials by creating a `.env` file and adding your credentials:

    ```plaintext
    REDDIT_USERNAME=your_username
    REDDIT_PASSWORD=your_password
    REDDIT_CLIENT_ID=your_client_id
    REDDIT_CLIENT_SECRET=your_client_secret
    GOOGLE_API_KEY=your_gemini_key
    ```

4. Run the bot:

    ```bash
    python main.py
    ```

## Contributing

Contributions to the Article Summarizer Bot project are welcome! If you find a bug or have a feature request, please open an issue. Pull requests are also appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
