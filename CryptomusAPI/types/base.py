from __future__ import annotations
from typing import Any


class Response:
    ...

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Response:
        raise NotImplementedError