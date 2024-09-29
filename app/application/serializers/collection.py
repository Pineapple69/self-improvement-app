from flask_restx import fields

from app.application.api import api
from app.application.serializers.release import ReleaseSerializer

CollectionSerializer = api.model(
    "Collection",
    {
        "user": fields.String(),
        "releases": fields.List(fields.Nested(ReleaseSerializer)),
    },
)
