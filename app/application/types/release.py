from datetime import datetime

from app.application.enums.release_type import ReleaseType
from app.application.models import Release


class BaseReleaseDto:
    type: ReleaseType
    genre: str
    release_date: datetime
    name: str
    artist_name: str

    def __init__(self, release: Release):
        self.type = release.type
        self.genre = release.genre
        self.release_date = release.release_date
        self.name = release.name
        self.artist_name = release.artist.name


class CreateReleaseDto(BaseReleaseDto):
    pass


class ReleaseDto(BaseReleaseDto):
    id: int

    def __init__(self, release: Release):
        super().__init__(release)
        self.id = release.id
