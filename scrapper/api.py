from datetime import datetime

import praw
from praw.models import ListingGenerator, MoreComments

from models.post import Post, PostCollection
from models.comment import Comment, CommentCollection


def get_subreddit_posts(reddit_client: praw.Reddit, subreddit_name: str) -> ListingGenerator:
        return reddit_client.subreddit(subreddit_name).top(time_filter='week', limit=10)


def get_top_posts(posts: ListingGenerator) -> PostCollection:
    post_collection = PostCollection()

    for p in posts:
        post = Post(
            id = p.fullname,
            title = p.title,
            author = 'Deleted user' if not p.author else p.author.name,
            score = p.score,
            upvote = p.ups,
            upvote_ratio = p.upvote_ratio,
            created_utc = datetime.utcfromtimestamp(p.created_utc),
        )
        post_collection.p_list.append(post)

    return post_collection.p_list


def get_top_comments(posts: ListingGenerator) -> CommentCollection:
    comments_collection = CommentCollection()

    for post in posts:
        for c in post.comments:
            if isinstance(c, MoreComments):
                continue
            comment = Comment(
                id = c.id,
                body = c.body,
                author = 'Deleted user' if not c.author else c.author.name,
                score = c.score,
                submission = c.submission,
                subreddit = c.subreddit,
                created_utc = datetime.utcfromtimestamp(c.created_utc),
            )
            comments_collection.c_list.append(comment)

    return comments_collection.c_list
