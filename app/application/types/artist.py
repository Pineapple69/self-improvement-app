from app.application.models import Artist
from app.application.types.release import ReleaseDto


class ArtistDto:
    name: str
    releases: ReleaseDto

    def __init__(self, artist: Artist):
        self.name = artist.name
        self.releases = [ReleaseDto(release) for release in artist.releases]
