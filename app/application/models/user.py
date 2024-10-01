from typing import TYPE_CHECKING, List

from flask_login import UserMixin
from sqlalchemy import Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.application.models.base_model import BaseModel, db, login_manager

if TYPE_CHECKING:
    from app.application.models import Collection, Role


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


user_role = Table(
    "user_role",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")),
)


class User(BaseModel, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]
    collection: Mapped["Collection"] = relationship(back_populates="user")
    roles: Mapped[List["Role"]] = relationship(secondary=user_role)
