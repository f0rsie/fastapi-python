from abc import ABC, abstractmethod
from typing import Any


class ModelBase(ABC):
    id: int

    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_fields(self) -> list[Any]:
        field_list: list[Any] = []

        for field in self.__dict__.keys():
            field_list.append(field)

        return field_list

    @abstractmethod
    def get_values(self) -> list[Any]:
        values_list: list[Any] = []

        for value in self.__dict__.keys():
            values_list.append(self.__dict__.get(value))

        return values_list
