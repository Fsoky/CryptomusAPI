from typing import TypeVar, Generic, Any, cast
import json

from adaptix import Retort

ResponseType = TypeVar("ResponseType")
retort = Retort()


class Method(Generic[ResponseType]):
    __returning__: type
    __api_method__: str
    __http_method__: str
    
    def to_str(self) -> str | None:
        return json.dumps(self.to_json())

    def to_json(self) -> dict[str, Any] | None:
        return cast(dict[str, Any], retort.dump(self))

    def build_response(self, json_string: str) -> ResponseType:
        return self.__returning__.from_json(json.loads(json_string))