from typing import TypedDict


class UserDto(TypedDict):
    username: str
    first_name: str
    last_name: str
    password: str
