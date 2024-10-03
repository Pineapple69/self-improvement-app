from flask import abort, request
from flask_login import current_user, login_required, login_user, logout_user
from flask_restx import Resource
from werkzeug.security import check_password_hash, generate_password_hash

from app.application.api import api
from app.application.models import Collection, Release, Role
from app.application.models.base_model import session
from app.application.models.user import User
from app.application.serializers.collection import CollectionSerializer
from app.application.serializers.release import AddReleaseToCollectionSerializer
from app.application.serializers.user import (
    UserLoginSerializer,
    UserSignUpSerializer,
)
from app.application.services.user import get_user_by_username
from app.application.types.collection import CollectionDto


class UserCollectionView(Resource):
    @api.marshal_with(CollectionSerializer)
    @login_required
    def get(self):
        return CollectionDto(current_user.collection), 200

    @api.expect(AddReleaseToCollectionSerializer)
    @login_required
    def post(self):
        release_to_add = session.get(Release, request.json["release_id"])
        if not release_to_add:
            return {"message": "Release does not exist"}, 200

        user_collection = current_user.collection
        releases = current_user.collection.releases

        if release_to_add in releases:
            return {
                "message": f"{release_to_add.name} already in collection"
            }, 200

        releases.append(release_to_add)
        user_collection.save()
        return {"message": f"{release_to_add.name} added to collection"}, 200

    @login_required
    def delete(self):
        release_to_delete = session.get(Release, request.json["release_id"])
        if not release_to_delete:
            return {"message": "Release does not exist"}, 304

        user_collection = current_user.collection
        releases = user_collection.releases

        try:
            release_index = releases.index(release_to_delete)
        except ValueError:
            return {
                "message": f"{release_to_delete.name} not in collection"
            }, 304

        del releases[release_index]
        user_collection.save()
        return {
            "message": f"{release_to_delete.name} deleted from collection"
        }, 200


class UserLoginView(Resource):
    @api.expect(UserLoginSerializer)
    def post(self):
        user_login = request.json
        username = user_login["username"]
        password = user_login["password"]
        user = get_user_by_username(username)
        if not user or not check_password_hash(user.password, password):
            abort(401)
        if not login_user(user):
            abort(400, "Login failed")

        return {"message": f"{username} successfully logged in"}, 200


class UserSignUpView(Resource):
    @api.expect(UserSignUpSerializer)
    def post(self):
        user_sign_in = request.json
        username = user_sign_in["username"]
        if get_user_by_username(username):
            abort(409, "User already exists")
        user_role = session.query(Role).filter_by(name="user").first()
        User(
            username=user_sign_in["username"],
            first_name=user_sign_in["first_name"],
            last_name=user_sign_in["last_name"],
            password=generate_password_hash(user_sign_in["password"]),
            collection=Collection(),
            roles=[user_role],
        ).save()
        return {"message": f"{username} signed up successfully"}, 200


class UserLogoutView(Resource):
    @login_required
    def post(self):
        if not logout_user():
            abort(400, "Logout failed")
        return {"message": "User logged out successfully"}, 200
