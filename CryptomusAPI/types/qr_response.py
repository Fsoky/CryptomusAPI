from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class QRCodeResponse:
    state: int
    image: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> QRCodeResponse:
        return cls(state=data["state"], image=data["image"])