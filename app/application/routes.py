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
    self_improvement.add_resource(UserLoginView, "/users/login")
    self_improvement.add_resource(UserLogoutView, "/users/logout")
    self_improvement.add_resource(UserSignUpView, "/users/signup")
    self_improvement.add_resource(UserCollectionView, "/users/collection")

    # collection
    self_improvement.add_resource(
        CollectionView, "/collections/<int:collection_id>", "/collections"
    )

    # artist
    self_improvement.add_resource(
        ArtistView, "/artists/<int:artist_id>", "/artists"
    )

    # release
    self_improvement.add_resource(
        ReleaseView, "/releases/<int:release_id>", "/releases"
    )
    self_improvement.add_resource(ReleaseGetAll, "/releases/get-all")
