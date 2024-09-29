from typing import TYPE_CHECKING, List

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.application.models.base_model import BaseModel, db

if TYPE_CHECKING:
    from app.application.models import Release, User

collection_release_association_table = Table(
    "collection_release_association_table",
    db.Model.metadata,
    Column("collection_id", ForeignKey("collection.id")),
    Column("release_id", ForeignKey("release.id")),
)


class Collection(BaseModel):
    __tablename__ = "collection"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    user: Mapped["User"] = relationship(
        back_populates="collection", single_parent=True
    )

    releases: Mapped[List["Release"]] = relationship(
        secondary=collection_release_association_table
    )
