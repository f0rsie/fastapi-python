from typing import Any
import json


class ModelBase:
    id: int

    def __init__(self):
        pass

    def get_fields(self) -> list[Any]:
        field_list: list[Any] = []

        for field in self.__dict__.keys():
            field_list.append(field)

        return field_list

    def get_values(self) -> list[Any]:
        values_list: list[Any] = []

        for value in self.__dict__.keys():
            values_list.append(self.__dict__.get(value))

        return values_list

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
