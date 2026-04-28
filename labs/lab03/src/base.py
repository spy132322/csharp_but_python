from __future__ import annotations

from lab01.src.validators import _validate_discount, _validate_name, _validate_price, _validate_stock, _validate_int
from lab04.src.interfaces import Printable, Comparable

class Product:
    __slots__ = ("_name", "_price", "_discount", "_stock", "_active")

    TAX_RATE = 0.20

    def __init__(self, name, price, discount=0.0, stock=0, active=True):
        self._name = _validate_name(name)
        self._price = _validate_price(price)
        self._discount = _validate_discount(discount)
        self._stock = _validate_stock(stock)
        self._active = bool(active)


    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = _validate_price(value)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = _validate_discount(value)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = _validate_stock(value)

    @property
    def active(self):
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def price_after_discount(self):
        return round(self._price * (1 - self._discount / 100), 2)

    def calculate_price(self):
        return self.price_after_discount()

    def price_with_tax(self):
        return round(self.calculate_price() * (1 + Product.TAX_RATE), 2)

    def purchase(self, quantity):
        quantity = _validate_int(quantity, "quantity", positive=True)
        if not self._active:
            raise RuntimeError("cannot purchase inactive product")
        if quantity > self._stock:
            raise ValueError("not enough stock")
        self._stock -= quantity
        return round(quantity * self.calculate_price(), 2)

    def restock(self, amount):
        amount = _validate_int(amount, "restock amount", positive=True)
        self._stock += amount

    def _identity_fields(self):
        return self._name, self._price, self._discount, self._stock, self._active

    def __str__(self):
        return (
            f"{self._name} | price: {self.calculate_price():.2f} | "
            f"tax price: {self.price_with_tax():.2f} | discount: {self._discount:.1f}% | "
            f"stock: {self._stock} | active: {self._active}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(name={self._name!r}, price={self._price!r}, "
            f"discount={self._discount!r}, stock={self._stock!r}, active={self._active!r})"
        )

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self._identity_fields() == other._identity_fields()