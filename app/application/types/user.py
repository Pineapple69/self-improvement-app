from app.application.models import User


class UserDto:
    id: int
    username: str
    first_name: str
    last_name: str

    def __init__(self, user: User):
        self.id = user.id
        self.username = user.username
        self.first_name = user.first_name
        self.last_name = user.last_name
