from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.application.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.application.models import Release


class Artist(BaseModel):
    __tablename__ = "artist"

    name: Mapped[str] = mapped_column(unique=True)
    releases: Mapped[List["Release"]] = relationship(back_populates="artist")
