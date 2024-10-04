from enum import Enum


class Statuses(Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    TESTING = "TESTING"
    CLOSED = "CLOSED"

    @classmethod
    def choices(cls):
        return [(status.name, status.value) for status in cls]
