from datetime import datetime
from typing import Any, TypeVar

from flask import abort
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()
login_manager = LoginManager()
session = db.session

T = TypeVar("T", bound="BaseModel")


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(
        db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now
    )

    @classmethod
    def get_or_abort(cls: type[T], id_: int) -> T:
        if instance := cls.query.get(id_):
            return instance
        abort(400, f"{cls.__name__}<id={id_}> was not found")

    def update(
        self: T,
        data: dict[str, Any] | None = None,
        /,
        mask: dict[str, str] | None = None,
        **kwargs_data: Any,
    ) -> T:
        data = (data or {}) | kwargs_data
        mask = mask or {}
        for key, value in data.items():
            key_with_mask = mask.get(key, key)
            setattr(self, key_with_mask, value)
        return self

    def save(self: T) -> T:
        self.add()
        self.commit()
        return self

    def delete(self) -> None:
        session.delete(self)
        self.commit()

    def add(self: T) -> T:
        session.add(self)
        return self

    @classmethod
    def commit(cls) -> None:
        session.commit()

    def to_dict(self):
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }

    def __str__(self) -> str:
        return f"<model_name: {self.__class__.__name__}, id: {self.id}>"

    def __repr__(self) -> str:
        fields = {}
        for name, value in vars(self).items():
            if not (name.startswith("_") or isinstance(value, classmethod)):
                fields[name] = value
        return f"<{str(fields)}>"
