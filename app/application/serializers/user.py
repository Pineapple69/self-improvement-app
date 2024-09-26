from flask_restx import fields

from app.application.api import api

UserSignUpSerializer = api.model(
    "UserSignIn",
    {
        "username": fields.String(),
        "password": fields.String(),
        "first_name": fields.String(),
        "last_name": fields.String(),
    },
)

UserLoginSerializer = api.model(
    "UserLogin", {"username": fields.String(), "password": fields.String()}
)
