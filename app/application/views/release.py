from flask import request
from flask_restx import Resource

from app.application.api import api
from app.application.models import Release
from app.application.models.base_model import session
from app.application.serializers.release import ReleaseSerializer
from app.application.services.release import create_release


class ReleaseGetByUserView(Resource):
    @api.marshal_with(ReleaseSerializer)
    def get(self, user_id: str):
        return session.get(Release, {"user_id": user_id})


class ReleaseView(Resource):
    @api.marshal_with(ReleaseSerializer)
    def get(self, release_id: str):
        return session.get(Release, release_id)

    @api.expect(ReleaseSerializer)
    @api.marshal_with(ReleaseSerializer)
    def post(self):
        release_dto = request.json
        return create_release(release_dto)

    def delete(self, release_id: str):
        return session.delete(Release, release_id)
