from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.application.enums.release_type import ReleaseType
from app.application.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.application.models import Artist


class Release(BaseModel):
    __tablename__ = "release"

    type: Mapped[ReleaseType]
    genre: Mapped[str]
    release_date: Mapped[datetime]
    name: Mapped[str]
    artist_id: Mapped[int] = mapped_column(ForeignKey("artist.id"))
    artist: Mapped["Artist"] = relationship(back_populates="releases")
