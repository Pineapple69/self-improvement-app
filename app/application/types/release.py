from datetime import datetime
from typing import TypedDict

from app.application.enums.release_type import ReleaseType


class BaseReleaseDto(TypedDict):
    type: ReleaseType
    genre: str
    release_date: datetime
    name: str
    artist_name: str


class CreateReleaseDto(BaseReleaseDto):
    pass


class ReleaseDto(BaseReleaseDto):
    id: int
