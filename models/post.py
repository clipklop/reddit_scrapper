import datetime
from dataclasses import dataclass, field


@dataclass
class Post:
    id: str # fullname
    title: str
    author: str
    score: int
    upvote: int
    upvote_ratio: float # The percentage of upvotes from all votes on the submission.
    created_utc: datetime.datetime


@dataclass
class PostCollection:
    p_list: list[Post] = field(default_factory=list)
