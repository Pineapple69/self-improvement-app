from flask import request
from flask_restx import Resource

from app.app import authorize
from app.application.api import api
from app.application.models import Artist
from app.application.models.base_model import session
from app.application.serializers.artist import (
    ArtistSerializer,
    CreateArtistSerializer,
)


class ArtistView(Resource):
    @api.marshal_with(ArtistSerializer)
    def get(self, artist_id: str):
        return session.get(Artist, artist_id)

    @api.expect(CreateArtistSerializer)
    @api.marshal_with(ArtistSerializer)
    @authorize.has_role("admin")
    def post(self):
        artist_name = request.json["name"]
        return Artist(name=artist_name).save()

    @authorize.has_role("admin")
    def delete(self, artist_id: str):
        return session.delete(Artist, artist_id)
