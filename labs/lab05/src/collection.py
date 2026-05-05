from typing import Callable, Iterable, Iterator
from functools import cmp_to_key


class ProductCatalog:
    def __init__(self, items: Iterable = ()):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def sort_by(self, key_func: Callable, reverse: bool = False):
        return ProductCatalog(sorted(self._items, key=key_func, reverse=reverse))

    def sort_by_comparable(self, reverse: bool = False):
        return ProductCatalog(
            sorted(self._items, key=cmp_to_key(lambda a, b: a.compare_to(b)), reverse=reverse)
        )

    def filter_by(self, predicate: Callable):
        return ProductCatalog(filter(predicate, self._items))

    def apply(self, func: Callable):
        return ProductCatalog(map(func, self._items))

    def get_printable(self):
        return ProductCatalog(filter(lambda x: hasattr(x, "to_string"), self._items))

    def __iter__(self) -> Iterator:
        return iter(self._items)

    def __repr__(self):
        return "\n".join(x.to_string() for x in self._items)
