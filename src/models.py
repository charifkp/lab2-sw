from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid


class Priority(Enum):
    HIGH = "HIGH"
    MID = "MID"
    LOW = "LOW"


class Status(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


@dataclass
class TodoItem:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    details: str = ""
    priority: Priority = Priority.MID
    status: Status = Status.PENDING
    owner: str = ""
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def __post_init__(self):
        # ensure enum values are of correct type
        if isinstance(self.priority, str):
            self.priority = Priority(self.priority)
        if isinstance(self.status, str):
            self.status = Status(self.status)
