from typing import Callable
from functools import cmp_to_key
from models import Product


def by_name(p: Product):
    return p.name.casefold()


def by_price(p: Product):
    return p.calculate_price()


def by_stock(p: Product):
    return p.stock


def by_type_then_price(p: Product):
    return p.__class__.__name__, p.calculate_price()


def by_comparable():
    return cmp_to_key(lambda a, b: a.compare_to(b))


def is_active(p: Product):
    return p.active


def is_in_stock(p: Product):
    return p.stock > 0


def is_type(product_type: type) -> Callable:
    def predicate(p: Product):
        return isinstance(p, product_type)
    return predicate


def is_expensive(min_price: float) -> Callable:
    def predicate(p: Product):
        return p.calculate_price() >= min_price
    return predicate


def apply_discount(percent: float) -> Callable:
    def fn(p: Product):
        p.discount = percent
        return p
    return fn


class DiscountStrategy:
    def __init__(self, percent: float):
        self.percent = percent

    def __call__(self, p: Product):
        p.discount = self.percent
        return p


class ActivateStrategy:
    def __call__(self, p: Product):
        p.activate()
        return p
