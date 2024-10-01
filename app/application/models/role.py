from flask_authorize import AllowancesMixin
from sqlalchemy.orm import Mapped

from app.application.models.base_model import BaseModel, db


class Role(BaseModel, AllowancesMixin):
    __tablename__ = "role"
    __allowances__ = "*"

    name: Mapped[str]
