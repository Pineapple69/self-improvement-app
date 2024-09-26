from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

from app.application.models.base_model import BaseModel, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(BaseModel, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    password: Mapped[str]
