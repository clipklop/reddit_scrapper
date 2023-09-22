import datetime
from dataclasses import dataclass, field


@dataclass
class Post:
    id: str
    name: str
    display_name: str
    author: str
    score: str
    created_utc: datetime.datetime
    description: str


@dataclass
class PostCollection:
    collection: list[Post]
    