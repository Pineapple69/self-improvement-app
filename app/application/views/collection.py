from flask_restx import Resource

from app.application.api import api
from app.application.models import Collection
from app.application.models.base_model import session
from app.application.serializers.collection import CollectionSerializer
from app.application.types.collection import CollectionDto


class CollectionView(Resource):
    @api.marshal_with(CollectionSerializer)
    def get(self, collection_id: str):
        collection = session.get(Collection, collection_id)
        return CollectionDto(collection)
