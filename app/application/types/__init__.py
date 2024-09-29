__version__ = "0.1.0"

from app.application.models.artist import Artist
from app.application.models.collection import (
    Collection,
    collection_release_association_table,
)
from app.application.models.release import Release
from app.application.models.user import User
