from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        raise NotImplementedError


class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other: object) -> int:
        raise NotImplementedError
