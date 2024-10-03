from flask import request
from flask_restx import Resource

from app.application.api import api
from app.application.models import Artist
from app.application.models.base_model import authorize, session
from app.application.serializers.artist import (
    ArtistSerializer,
    CreateArtistSerializer,
)
from app.application.types.artist import ArtistDto


class ArtistView(Resource):
    @api.marshal_with(ArtistSerializer)
    def get(self, artist_id: str):
        return ArtistDto(session.get(Artist, artist_id))

    @api.expect(CreateArtistSerializer)
    @api.marshal_with(ArtistSerializer)
    @authorize.has_role("admin")
    def post(self):
        artist_name = request.json["name"]
        return ArtistDto(Artist(name=artist_name).save())

    @authorize.has_role("admin")
    def delete(self, artist_id: str):
        return session.delete(session.get(Artist, artist_id))
