#

import os
import json

import praw

from models.post import Post

# def show_request_urls():
#     # driver.get(target_url)
#     # return [{"url": r.url} for r in driver.requests]0
#     reddit = praw.Reddit("bot", user_agent="bot2 user agent")
#     print(reddit)


def get_top_posts(reddit: praw.Reddit) -> None:
    # top_posts = reddit.subreddit("all").top(limit=10)
    top_posts = reddit.subreddit("learnpython").top(limit=10)

    for post in top_posts:
        print(post.num_comments)


def get_top_comments(reddit: praw.Reddit) -> None:
    post = next(reddit.subreddit("all").top(limit=1))
    top_comments = post.comments.list()[:5]
    
    for comment in top_comments:
        print(comment.body)


def main() -> None:
    reddit = praw.Reddit("bot")

    print(Post)
    # get_top_posts(reddit)
    # get_top_comments(reddit)
    # print(reddit)


if __name__ == '__main__':
    main()
