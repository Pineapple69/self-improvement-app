from flask import request
from flask_restx import Resource

from app.application.api import api
from app.application.models import Release
from app.application.models.base_model import authorize, session
from app.application.serializers.release import ReleaseSerializer
from app.application.services.release import create_release
from app.application.types.release import ReleaseDto


class ReleaseGetAll(Resource):
    @api.marshal_list_with(ReleaseSerializer)
    def get(self):
        releases = session.query(Release).all()
        return [ReleaseDto(release) for release in releases]


class ReleaseView(Resource):
    @api.marshal_with(ReleaseSerializer)
    def get(self, release_id: str):
        return ReleaseDto(session.get(Release, release_id))

    @api.expect(ReleaseSerializer)
    @api.marshal_with(ReleaseSerializer)
    @authorize.has_role("admin")
    def post(self):
        create_release_dto = request.json
        return create_release(create_release_dto)

    @authorize.has_role("admin")
    def delete(self, release_id: str):
        return session.delete(session.get(Release, release_id))
