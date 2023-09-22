#

import os
import json

import praw

from models.post import Post, PostCollection

# def show_request_urls():
#     # driver.get(target_url)
#     # return [{"url": r.url} for r in driver.requests]0
#     reddit = praw.Reddit("bot", user_agent="bot2 user agent")
#     print(reddit)


def get_top_posts(reddit: praw.Reddit) -> None:
    # top_posts = reddit.subreddit("all").top(limit=10)
    top_posts = reddit.subreddit("learnpython").top(limit=10)

    for post in top_posts:
        # print(post.num_comments)
        # post returns
        # 'STR_FIELD', 'add_fetch_param', 'all_awardings', 'allow_live_comments', 'approved_at_utc', 'approved_by',
        # 'archived', 'author', 'author_flair_background_color', 'author_flair_css_class', 'author_flair_richtext',
        # 'author_flair_template_id', 'author_flair_text', 'author_flair_text_color', 'author_flair_type', 'author_fullname',
        #  'author_is_blocked', 'author_patreon_flair', 'author_premium', 'award', 'awarders', 'banned_at_utc', 'banned_by',
        #  'can_gild', 'can_mod_post', 'category', 'clear_vote', 'clicked', 'comment_limit', 'comment_sort', 'comments',
        #  'content_categories', 'contest_mode', 'created', 'created_utc', 'crosspost', 'delete', 'disable_inbox_replies',
        #  'discussion_type', 'distinguished', 'domain', 'downs', 'downvote', 'duplicates', 'edit', 'edited', 'enable_inbox_replies',
        #  'flair', 'fullname', 'gild', 'gilded', 'gildings', 'hidden', 'hide', 'hide_score', 'id', 'id_from_url',
        #  'is_created_from_ads_ui', 'is_crosspostable', 'is_meta', 'is_original_content', 'is_reddit_media_domain', 'is_robot_indexable',
        #  'is_self', 'is_video', 'likes', 'link_flair_background_color', 'link_flair_css_class', 'link_flair_richtext', 'link_flair_text',
        #  'link_flair_text_color', 'link_flair_type', 'locked', 'mark_visited', 'media', 'media_embed', 'media_only', 'mod', 'mod_note',
        #  'mod_reason_by', 'mod_reason_title', 'mod_reports', 'name', 'no_follow', 'num_comments', 'num_crossposts', 'num_reports',
        #  'over_18', 'parent_whitelist_status', 'parse', 'permalink', 'pinned', 'pwls', 'quarantine', 'removal_reason', 'removed_by',
        #  'removed_by_category', 'reply', 'report', 'report_reasons', 'save', 'saved', 'score', 'secure_media', 'secure_media_embed',
        #  'selftext', 'selftext_html', 'send_replies', 'shortlink', 'spoiler', 'stickied', 'subreddit', 'subreddit_id',
        #  'subreddit_name_prefixed', 'subreddit_subscribers', 'subreddit_type', 'suggested_sort', 'thumbnail', 'title', 'top_awarded_type',
        #  'total_awards_received', 'treatment_tags', 'unhide', 'unsave', 'ups', 'upvote', 'upvote_ratio', 'url', 'user_reports',
        #  'view_count', 'visited', 'whitelist_status', 'wls'
        print(
            post.id,
            post.name,
            post.author,
            post.fullname,
            post.score,
            post.created_utc,
        )


def get_top_comments(reddit: praw.Reddit) -> None:
    post = next(reddit.subreddit("all").top(limit=1))
    top_comments = post.comments.list()[:5]
    
    for comment in top_comments:
        print(comment.body)


def main() -> None:
    reddit = praw.Reddit("bot")

    # print(Post)
    get_top_posts(reddit)
    # get_top_comments(reddit)
    # print(reddit)


if __name__ == '__main__':
    main()