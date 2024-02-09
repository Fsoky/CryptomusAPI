from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class RefundResponse:
    state: int
    result: list

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> RefundResponse:
        return cls(state=data["state"], **data["result"])