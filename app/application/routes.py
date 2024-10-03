from app.application.namespaces import self_improvement
from app.application.views.artist import ArtistView
from app.application.views.collection import CollectionView
from app.application.views.release import ReleaseGetAll, ReleaseView
from app.application.views.user import (
    UserCollectionView,
    UserLoginView,
    UserLogoutView,
    UserSignUpView,
)


def init_routes() -> None:
    # user
    self_improvement.add_resource(UserLoginView, "/user/login")
    self_improvement.add_resource(UserLogoutView, "/user/logout")
    self_improvement.add_resource(UserSignUpView, "/user/signup")
    self_improvement.add_resource(UserCollectionView, "/user/collection")

    # collection
    self_improvement.add_resource(
        CollectionView, "/collection/<int:collection_id>", "/collection"
    )

    # artist
    self_improvement.add_resource(
        ArtistView, "/artist/<int:artist_id>", "/artist"
    )

    # release
    self_improvement.add_resource(
        ReleaseView, "/release/<int:release_id>", "/release"
    )
    self_improvement.add_resource(ReleaseGetAll, "/release/get-all")
