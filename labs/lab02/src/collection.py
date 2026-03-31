from __future__ import annotations

from typing import Callable, Iterable, Iterator, Optional

from lab01.src.model import Product


class ProductCatalog:
    def __init__(self, items: Optional[Iterable[Product]] = None):
        self._items: list[Product] = []
        if items is not None:
            for item in items:
                self.add(item)

    @staticmethod
    def _validate_product(item: object) -> Product:
        if not isinstance(item, Product):
            raise TypeError("can add only Product")
        return item

    @staticmethod
    def _validate_name(name: object) -> str:
        if not isinstance(name, str):
            raise TypeError("name must be str")
        if not name:
            raise ValueError("name must be non-empty")
        return name

    @staticmethod
    def _validate_number(value: object, field_name: str) -> float:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"{field_name} must be numeric")
        return float(value)

    @staticmethod
    def _validate_index(index: object) -> int:
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("index must be int")
        return index

    def _find_index_by_name(self, name: str) -> int:
        for index, item in enumerate(self._items):
            if item.name == name:
                return index
        return -1

    def add(self, item: Product) -> None:
        item = self._validate_product(item)
        if self._find_index_by_name(item.name) != -1:
            raise ValueError("duplicate product name")
        self._items.append(item)

    def remove(self, item: Product) -> None:
        item = self._validate_product(item)
        index = self._find_index_by_name(item.name)
        if index == -1:
            raise ValueError("item not found")
        del self._items[index]

    def remove_at(self, index: int) -> Product:
        index = self._validate_index(index)
        return self._items.pop(index)

    def get_all(self) -> list[Product]:
        return list(self._items)

    def find_by_name(self, name: str) -> Optional[Product]:
        name = self._validate_name(name)
        index = self._find_index_by_name(name)
        if index == -1:
            return None
        return self._items[index]

    def sort(
        self,
        key: Optional[Callable[[Product], object]] = None,
        reverse: bool = False,
    ) -> ProductCatalog:
        if key is None:
            key = lambda item: item.name.casefold()
        self._items.sort(key=key, reverse=reverse)
        return self

    def sort_by_name(self, reverse: bool = False) -> ProductCatalog:
        return self.sort(key=lambda item: item.name.casefold(), reverse=reverse)

    def sort_by_price(self, reverse: bool = False) -> ProductCatalog:
        return self.sort(key=lambda item: item.price_after_discount(), reverse=reverse)

    def get_active(self) -> ProductCatalog:
        return self.__class__(item for item in self._items if item.active)

    def get_available(self) -> ProductCatalog:
        return self.__class__(item for item in self._items if item.active and item.stock > 0)

    def get_expensive(self, min_price: float) -> ProductCatalog:
        threshold = self._validate_number(min_price, "min_price")
        return self.__class__(
            item for item in self._items if item.price_after_discount() >= threshold
        )

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[Product]:
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        if isinstance(index, slice):
            return self.__class__(result)
        return result

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._items!r})"
