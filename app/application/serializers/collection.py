from flask_restx import fields

from app.application.api import api
from app.application.serializers.release import ReleaseSerializer
from app.application.serializers.user import UserSerializer

CollectionSerializer = api.model(
    "Collection",
    {
        "user": fields.Nested(UserSerializer),
        "releases": fields.List(fields.Nested(ReleaseSerializer)),
    },
)
