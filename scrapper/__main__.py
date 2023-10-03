from pprint import pprint

import praw
from prawcore.exceptions import ResponseException

from models.subreddit import Subreddit

from scrapper.api import get_subreddit_posts, get_top_posts, get_top_comments


def main() -> None:
    reddit = praw.Reddit("bot")
    subreddit_posts = get_subreddit_posts(reddit, Subreddit.ALL.value)

    try:
        print("Top posts:")
        top_posts = get_top_posts(posts=subreddit_posts)
        pprint(top_posts)
        
        print("Top comments:")
        subreddit_posts = get_subreddit_posts(reddit, Subreddit.ALL.value)
        top_comments = get_top_comments(posts=subreddit_posts)
        pprint(top_comments)
    except ResponseException as e:
        print(e)


if __name__ == '__main__':
    main()
