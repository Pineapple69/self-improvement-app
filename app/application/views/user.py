from flask import abort, request
from flask_login import login_required, login_user, logout_user
from flask_restx import Resource
from werkzeug.security import check_password_hash, generate_password_hash

from app.application.api import api
from app.application.models.user import User
from app.application.serializers.user import (
    UserLoginSerializer,
    UserSignUpSerializer,
)
from app.application.services.user import get_user_by_username


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
            abort(400, message="Login failed")

        return {"message": f"{username} successfully logged in"}, 200


class UserSignUpView(Resource):
    @api.expect(UserSignUpSerializer)
    def post(self):
        user_sign_in = request.json
        username = user_sign_in["username"]
        if get_user_by_username(username):
            abort(409, message="User already exists")
        User(
            username=user_sign_in["username"],
            first_name=user_sign_in["first_name"],
            last_name=user_sign_in["last_name"],
            password=generate_password_hash(user_sign_in["password"]),
        ).save()
        return {"message": f"{username} signed up successfully"}, 200


class UserLogoutView(Resource):
    @login_required
    def post(self):
        if not logout_user():
            abort(400, "Logout failed")
        return {"message": "User logged out successfully"}, 200
