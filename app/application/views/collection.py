from flask_restx import Resource

from app.application.api import api
from app.application.models import Collection
from app.application.models.base_model import session
from app.application.serializers.collection import CollectionSerializer


class CollectionView(Resource):
    @api.marshal_with(CollectionSerializer)
    def get(self, collection_id: str):
        return session.get(Collection, collection_id)
