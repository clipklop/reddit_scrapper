import praw

from models.post import Post

from .api_scrapper import get_top_posts

def main() -> None:
    reddit = praw.Reddit("bot")

    post = Post(
        'id',
        'name',
        'display_name','author',
        'score',
        'created_utc',
        'description'
    )
    
    print(post.id)
    # get_top_posts(reddit)
    # get_top_comments(reddit)
    # print(reddit)


if __name__ == '__main__':
    main()
