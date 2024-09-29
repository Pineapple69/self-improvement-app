from enum import Enum


class ReleaseType(str, Enum):
    SINGLE = "single"
    LP = "lp"
    EP = "ep"
    COMPILATION = "compilation"
