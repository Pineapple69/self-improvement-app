from flask_restx import fields

from app.application.api import api
from app.application.serializers.release import ReleaseSerializer

CreateArtistSerializer = api.model("CreateArtist", {"name": fields.String()})

ArtistSerializer = api.model(
    "Artist",
    {
        "name": fields.String(),
        "releases": fields.List(fields.Nested(ReleaseSerializer)),
    },
)
