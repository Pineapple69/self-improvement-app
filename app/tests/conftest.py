from typing import Dict, Generator

import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import close_all_sessions

from app.app import init_app
from app.application.models import Role
from app.application.models.base_model import db as db_


@pytest.fixture()
def app_url():
    return "/api/self-improvement"


@pytest.fixture(scope="session", autouse=True)
def roles() -> Dict[str, Role]:
    return {
        "admin_role": Role(name="admin", allowances={}).save(),
        "user_role": Role(
            name="user",
            allowances={"artist": "r", "release": "r", "collection": "r"},
        ).save(),
    }


@pytest.fixture(scope="session")
def app() -> Generator[Flask, None, None]:
    test_app = Flask(__name__)
    init_app(test_app)
    test_app.config.update({"TESTING": True})

    yield test_app


@pytest.fixture(scope="session")
def api_client(app: Flask) -> Generator[FlaskClient, None, None]:
    with app.test_client() as test_client:
        yield test_client


@pytest.fixture(scope="session", autouse=True)
def database(app: Flask) -> Generator[SQLAlchemy, None, None]:
    with app.app_context():
        db_.create_all()
        yield db_
        close_all_sessions()
        db_.drop_all()


@pytest.fixture(scope="function", autouse=True)
def db(  # pylint: disable=redefined-outer-name,invalid-name
    database: SQLAlchemy, monkeypatch: pytest.MonkeyPatch
) -> Generator[SQLAlchemy, None, None]:
    """
    IMPORTANT: This rollback DOES NOT affect `Sequence`. Read more here:
    https://communities.actian.com/s/article/Rollback-and-Sequence-Values
    """
    _rollback = database.session.rollback

    def _commit():
        try:
            database.session.flush()
            database.session.expire_all()
        except Exception as exc:
            _rollback()
            raise exc

    monkeypatch.setattr(database.session, "commit", _commit)
    monkeypatch.setattr(database.session, "remove", lambda: None)
    monkeypatch.setattr(database.session, "rollback", lambda: None)
    yield database
    _rollback()
    database.session.remove()
