import pytest
from werkzeug.security import generate_password_hash

from app.application.models import Artist, Collection, Release, User

USERNAME = "username"
PASSWORD = "password"


@pytest.fixture()
def logged_in_user(api_client, app_url, roles) -> User:
    user = User(
        username=USERNAME,
        first_name="",
        last_name="",
        password=generate_password_hash(PASSWORD),
        collection=Collection(),
        roles=[roles.get("user_role")],
    ).save()
    api_client.post(
        f"{app_url}/user/login", json=dict(username=USERNAME, password=PASSWORD)
    )
    return user


@pytest.fixture()
def releases():
    artist = Artist(name="Nanahira").save()
    return [
        Release(
            type="LP",
            genre="Denpa",
            release_date="12/29/2017",
            name="4orce!",
            artist=artist,
        ).save(),
        Release(
            type="LP",
            genre="Denpa",
            release_date="12/31/2016",
            name="Secretale",
            artist=artist,
        ).save(),
        Release(
            type="LP",
            genre="Denpa",
            release_date="08/12/2019",
            name="GOIN'!",
            artist=artist,
        ).save(),
    ]


def test_user_get_empty_collection(api_client, app_url, logged_in_user):
    res = api_client.get(f"{app_url}/user/collection")
    assert res.status_code == 200
    assert res.json["user"].get("id") == logged_in_user.id
    assert res.json["releases"] == []


def test_user_edit_release_to_collection(
    api_client, app_url, logged_in_user, releases
):
    release = releases[0]
    res = api_client.post(
        f"{app_url}/user/collection", json=dict(release_id=release.id)
    )
    assert res.status_code == 200
    assert res.json["message"] == f"{release.name} added to collection"

    res = api_client.get(f"{app_url}/user/collection")
    assert res.status_code == 200
    assert res.json["releases"] == [
        dict(
            type="ReleaseType.LP",
            genre="Denpa",
            release_date="2017-12-29T00:00:00",
            name="4orce!",
            artist_name="Nanahira",
            id=release.id,
        )
    ]

def test_user_delete_from_collection(
    api_client, app_url, logged_in_user, releases
):
    release = releases[0]
    res = api_client.post(
        f"{app_url}/user/collection", json=dict(release_id=release.id)
    )
    assert res.status_code == 200

    res = api_client.get(f"{app_url}/user/collection")
    assert res.status_code == 200
    assert len(res.json["releases"]) > 0

    res = api_client.delete(f"{app_url}/user/collection", json=dict(release_id=release.id))
    assert res.status_code == 200
    assert res.json["message"] == f"{release.name} deleted from collection"

    res = api_client.get(f"{app_url}/user/collection")
    assert res.status_code == 200
    assert res.json["releases"] == []
