from __future__ import annotations

from abc import ABC, abstractmethod


class Printable(ABC):
    """Контракт: объект можно представить в виде строки для вывода."""

    @abstractmethod
    def to_string(self) -> str:
        """Вернуть строковое представление объекта."""
        raise NotImplementedError


class Comparable(ABC):
    """Контракт: объект можно сравнивать с другим объектом того же домена."""

    @abstractmethod
    def compare_to(self, other: object) -> int:
        """
        Сравнить объект с другим:
        < 0  — меньше
        = 0  — равно
        > 0  — больше
        """
        raise NotImplementedError