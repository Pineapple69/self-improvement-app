import pytest
from werkzeug.security import generate_password_hash

from app.application.models import Artist, Collection, User

USER_USERNAME = "username"
USER_PASSWORD = "username"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"


@pytest.fixture(autouse=True)
def users_with_roles(roles):
    User(
        username=ADMIN_USERNAME,
        first_name="",
        last_name="",
        password=generate_password_hash(ADMIN_PASSWORD),
        collection=Collection(),
        roles=[roles.get("admin_role")],
    ).save()
    User(
        username=USER_USERNAME,
        first_name="",
        last_name="",
        password=generate_password_hash(USER_PASSWORD),
        collection=Collection(),
        roles=[roles.get("user_role")],
    ).save()


@pytest.fixture()
def artist() -> Artist:
    return Artist(name="artist").save()


def test_user_post_on_restricted_resource(api_client, app_url):
    api_client.post(
        f"{app_url}/user/login",
        json=dict(username=USER_USERNAME, password=USER_PASSWORD),
    )
    res = api_client.post(f"{app_url}/artist", json=dict(name="artist"))
    assert res.status_code == 401


def test_admin_post_on_restricted_resource(api_client, app_url):
    api_client.post(
        f"{app_url}/user/login",
        json=dict(username=ADMIN_USERNAME, password=ADMIN_PASSWORD),
    )
    res = api_client.post(f"{app_url}/artist", json=dict(name="artist"))
    assert res.status_code == 200


def test_user_delete_on_restricted_resource(api_client, app_url, artist):
    api_client.post(
        f"{app_url}/user/login",
        json=dict(username=USER_USERNAME, password=USER_PASSWORD),
    )
    res = api_client.delete(f"{app_url}/artist/{artist.id}")
    assert res.status_code == 401


def test_admin_delete_on_restricted_resource(api_client, app_url, artist):
    api_client.post(
        f"{app_url}/user/login",
        json=dict(username=ADMIN_USERNAME, password=ADMIN_PASSWORD),
    )
    res = api_client.delete(f"{app_url}/artist/{artist.id}")
    assert res.status_code == 200
