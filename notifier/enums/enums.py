from enum import Enum


class EmailTypeEnum(str, Enum):
    REGISTRATION: str = "REGISTRATION"
    RESTORE_ACCESS: str = "RESTORE_ACCESS"
