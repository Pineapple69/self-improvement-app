from typing import List

from app.application.models import Collection
from app.application.types.release import ReleaseDto
from app.application.types.user import UserDto


class CollectionDto:
    user: UserDto
    releases: List[ReleaseDto]

    def __init__(self, collection: Collection):
        self.user = UserDto(collection.user)
        self.releases = [ReleaseDto(release) for release in collection.releases]
