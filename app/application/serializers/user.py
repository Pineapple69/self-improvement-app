from flask_restx import fields

from app.application.api import api

UserBaseSerializer = {
    "username": fields.String(),
    "first_name": fields.String(),
    "last_name": fields.String(),
}

UserSerializer = api.model(
    "UserSerializer",
    UserBaseSerializer
    | {
        "id": fields.Integer(),
    },
)

UserSignUpSerializer = api.model(
    "UserSignIn",
    UserBaseSerializer
    | {
        "password": fields.String(),
    },
)

UserLoginSerializer = api.model(
    "UserLogin", {"username": fields.String(), "password": fields.String()}
)
