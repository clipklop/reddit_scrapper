from dataclasses import asdict
from collections import Counter

from models.post import PostCollection
from models.comment import CommentCollection


def author_counter(reddit_collections: PostCollection | CommentCollection) -> Counter:
    counter = Counter()
 
    for collection in reddit_collections:
        collection = asdict(collection)
        if collection['author'] in counter:
            counter[collection['author']] += 1
        else:
            counter[collection['author']] = 1

    return counter
