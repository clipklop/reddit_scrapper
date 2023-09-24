#

import os
import enum
import json
from datetime import datetime
from dataclasses import asdict, astuple
from collections import Counter


import praw

from models.post import Post, PostCollection

# def show_request_urls():
#     # driver.get(target_url)
#     # return [{"url": r.url} for r in driver.requests]0
#     reddit = praw.Reddit("bot", user_agent="bot2 user agent")
#     print(reddit)

class Subreddit(enum.Enum):
    ALL = 'all'
    PY = 'learnpython'


def get_top_posts(reddit_client: praw.Reddit, subreddit_name: str) -> PostCollection:
    top_posts = reddit_client.subreddit(subreddit_name).top(time_filter='week')#, limit=10)
    post_collection = PostCollection()

    for p in top_posts:
        post = Post(
            id = p.fullname,
            title = p.title,
            author = p.author.name,
            score = p.score,
            upvote = p.ups,
            upvote_ratio = p.upvote_ratio,
            created_utc = datetime.utcfromtimestamp(p.created_utc),
        )
        post_collection.p_list.append(post)

    return post_collection.p_list


def post_author_counter(post_collection: PostCollection) -> Counter[str]:
    counter = Counter()

    for post in post_collection:
        post = asdict(post)
        if post['author'] in counter:
            counter[post['author']] += 1
        else:
            counter[post['author']] = 0

    return counter


def get_top_comments(reddit: praw.Reddit) -> None:
    # post = next(reddit.subreddit("all").top(limit=1))

    top_post = reddit.subreddit("all").top(limit=1)
    top_comments = [i.comments for i in top_post]

    for comment in top_comments:
        if isinstance(comment, praw.models.MoreComments):
            continue
        print(comment.body)

    # for comment in top_comments:
    #     print(comment.body)


def main() -> None:
    
    reddit = praw.Reddit("bot")
    
    # post = get_top_posts(reddit_client=reddit, subreddit_name=Subreddit.ALL.value)
    # print(post_author_counter(post).most_common())

    get_top_comments(reddit)
    # print(reddit)


if __name__ == '__main__':
    main()
