from flask import abort

from app.application.models import Artist, Release
from app.application.models.base_model import session
from app.application.types.release import CreateReleaseDto, ReleaseDto


def create_release(create_release_dto: CreateReleaseDto) -> ReleaseDto:
    artist_name = create_release_dto.artist_name
    artist = session.query(Artist).filter_by(name=artist_name).first()
    if not artist:
        abort(400, f"Artist {artist_name} does not exist")
    return ReleaseDto(
        Release(
            type=create_release_dto.type,
            genre=create_release_dto.genre,
            release_date=create_release_dto.release_date,
            name=create_release_dto.name,
            artist=artist,
        ).save()
    )
