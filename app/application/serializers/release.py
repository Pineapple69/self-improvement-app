from flask_restx import fields

from app.application.api import api
from app.application.enums.release_type import ReleaseType

BaseReleaseSerializer = {
    "type": fields.String(enum=ReleaseType),
    "genre": fields.String(),
    "release_date": fields.DateTime(),
    "name": fields.String(),
}

ReleaseSerializer = api.model(
    "Release",
    BaseReleaseSerializer | {"artist_name": fields.String()},
)

AddReleaseToCollectionSerializer = api.model(
    "AddReleaseToCollection", {"release_id": fields.Integer()}
)
