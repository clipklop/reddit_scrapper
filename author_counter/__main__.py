from pprint import pprint

import praw
from prawcore.exceptions import ResponseException

from models.subreddit import Subreddit

from scrapper.api import get_subreddit_posts, get_top_posts, get_top_comments

from author_counter.author_counter import author_counter


def main() -> None:
    reddit = praw.Reddit("bot")
    subreddit_posts = get_subreddit_posts(reddit, Subreddit.ALL.value)

    try:
        print('- Top posts users')
        top_posts = get_top_posts(posts=subreddit_posts)
        pprint(author_counter(top_posts).most_common(5))

        print('---')

        print('- Top comments users')
        subreddit_posts = get_subreddit_posts(reddit, Subreddit.ALL.value)
        top_comments = get_top_comments(posts=subreddit_posts)
        pprint(author_counter(top_comments).most_common(5))

    except ResponseException as e:
        print(e)


if __name__ == '__main__':
    main()
