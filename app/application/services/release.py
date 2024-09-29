from app.application.models import Artist, Release
from app.application.models.base_model import session
from app.application.types.release import CreateReleaseDto, ReleaseDto


def create_release(create_release_dto: CreateReleaseDto) -> ReleaseDto:
    artist = (
        session.query(Artist)
        .filter_by(name=create_release_dto.get("artist_name"))
        .first()
    )
    release = Release(
        type=create_release_dto.get("type"),
        genre=create_release_dto.get("genre"),
        release_date=create_release_dto.get("release_date"),
        name=create_release_dto.get("name"),
        artist=artist,
    ).save()
    return ReleaseDto(
        id=release.id,
        type=release.type,
        genre=release.genre,
        release_date=release.release_date,
        name=release.name,
        artist_name=release.artist.name,
    )
