from app.application.namespaces import self_improvement
from app.application.views.user import (
    UserLoginView,
    UserLogoutView,
    UserSignUpView,
)


def init_routes() -> None:
    self_improvement.add_resource(UserLoginView, "/user/login")
    self_improvement.add_resource(UserLogoutView, "/user/logout")
    self_improvement.add_resource(UserSignUpView, "/user/signup")
