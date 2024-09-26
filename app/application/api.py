from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)

authorizations = {
    "Bearer": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
        "description": (
            "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**,"
            " where JWT is the token"
        ),
    }
}


api = Api(
    blueprint,
    authorizations=authorizations,
    version="1.0.0",
    title="Self Improvement App API",
    description="An api for a raise",
)
