from __future__ import annotations

from lab01.src.validators import (
    _validate_discount,
    _validate_int,
    _validate_name,
    _validate_number,
    _validate_price,
    _validate_stock,
)

from .interfaces import Comparable, Printable

class Product(Printable, Comparable):
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

    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other: object) -> int:
        if not isinstance(other, Product):
            raise TypeError("can compare only Product")

        self_value = self.calculate_price()
        other_value = other.calculate_price()
        return (self_value > other_value) - (self_value < other_value)

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


class LiquidProduct(Product):
    __slots__ = ("_volume_liters", "_bottle_fee")

    def __init__(
        self,
        name,
        price,
        discount=0.0,
        stock=0,
        active=True,
        volume_liters=1.0,
        bottle_fee=0.0,
    ):
        super().__init__(name, price, discount, stock, active)
        self._volume_liters = _validate_number(volume_liters, "volume_liters", positive=True)
        self._bottle_fee = _validate_number(bottle_fee, "bottle_fee", non_negative=True)

    @property
    def volume_liters(self):
        return self._volume_liters

    @property
    def bottle_fee(self):
        return self._bottle_fee

    def dilute(self, extra_liters):
        extra_liters = _validate_number(extra_liters, "extra_liters", positive=True)
        self._volume_liters += extra_liters
        return self._volume_liters

    def calculate_price(self):
        return round(self.price_after_discount() * self._volume_liters + self._bottle_fee, 2)

    def to_string(self) -> str:
        return (
            f"[LIQUID] {self.name} | volume: {self._volume_liters:.2f} l | "
            f"bottle fee: {self._bottle_fee:.2f} | price: {self.calculate_price():.2f} | "
            f"stock: {self.stock} | active: {self.active}"
        )

    def _identity_fields(self):
        return super()._identity_fields() + (self._volume_liters, self._bottle_fee)

    def __str__(self):
        return self.to_string()


class TangibleProduct(Product):
    __slots__ = ("_weight_kg", "_logistics_fee")

    def __init__(
        self,
        name,
        price,
        discount=0.0,
        stock=0,
        active=True,
        weight_kg=1.0,
        logistics_fee=0.0,
    ):
        super().__init__(name, price, discount, stock, active)
        self._weight_kg = _validate_number(weight_kg, "weight_kg", positive=True)
        self._logistics_fee = _validate_number(logistics_fee, "logistics_fee", non_negative=True)

    @property
    def weight_kg(self):
        return self._weight_kg

    @property
    def logistics_fee(self):
        return self._logistics_fee

    def add_packaging(self, extra_fee):
        extra_fee = _validate_number(extra_fee, "extra_fee", positive=True)
        self._logistics_fee += extra_fee
        return self._logistics_fee

    def calculate_price(self):
        return round(self.price_after_discount() + self._weight_kg * self._logistics_fee, 2)

    def to_string(self) -> str:
        return (
            f"[TANGIBLE] {self.name} | weight: {self._weight_kg:.2f} kg | "
            f"logistics fee: {self._logistics_fee:.2f} | price: {self.calculate_price():.2f} | "
            f"stock: {self.stock} | active: {self.active}"
        )

    def _identity_fields(self):
        return super()._identity_fields() + (self._weight_kg, self._logistics_fee)

    def __str__(self):
        return self.to_string()


class ServiceProduct(Product):
    __slots__ = ("_hours", "_complexity")

    def __init__(
        self,
        name,
        price,
        discount=0.0,
        stock=0,
        active=True,
        hours=1.0,
        complexity=1.0,
    ):
        super().__init__(name, price, discount, stock, active)
        self._hours = _validate_number(hours, "hours", positive=True)
        self._complexity = _validate_number(complexity, "complexity", positive=True)

    @property
    def hours(self):
        return self._hours

    @property
    def complexity(self):
        return self._complexity

    def extend_duration(self, extra_hours):
        extra_hours = _validate_number(extra_hours, "extra_hours", positive=True)
        self._hours += extra_hours
        return self._hours

    def calculate_price(self):
        return round(self.price_after_discount() * self._hours * self._complexity, 2)

    def to_string(self) -> str:
        return (
            f"[SERVICE] {self.name} | hours: {self._hours:.2f} | complexity: {self._complexity:.2f} | "
            f"price: {self.calculate_price():.2f} | stock: {self.stock} | active: {self.active}"
        )

    def _identity_fields(self):
        return super()._identity_fields() + (self._hours, self._complexity)

    def __str__(self):
        return self.to_string()