import datetime
from dataclasses import dataclass, field


@dataclass
class Comment:
    id: str # fullname
    body: str
    author: str
    score: int
    submission: str
    subreddit: str
    created_utc: datetime.datetime


@dataclass
class CommentCollection:
    c_list: list[Comment] = field(default_factory=list)
