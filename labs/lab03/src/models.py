from __future__ import annotations

from .base import Product
from lab01.src.validators import _validate_number


class LiquidProduct(Product):
    __slots__ = ("_volume_liters", "_bottle_fee")

    def __init__(self, name, price, discount=0.0, stock=0, active=True, volume_liters=1.0, bottle_fee=0.0):
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

    def _identity_fields(self):
        return super()._identity_fields() + (self._volume_liters, self._bottle_fee)

    def __str__(self):
        return (
            f"{self.name} | liquid | volume: {self._volume_liters:.2f} l | bottle fee: {self._bottle_fee:.2f} | "
            f"price: {self.calculate_price():.2f} | stock: {self.stock} | active: {self.active}"
        )


class TangibleProduct(Product):
    __slots__ = ("_weight_kg", "_logistics_fee")

    def __init__(self, name, price, discount=0.0, stock=0, active=True, weight_kg=1.0, logistics_fee=0.0):
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

    def _identity_fields(self):
        return super()._identity_fields() + (self._weight_kg, self._logistics_fee)

    def __str__(self):
        return (
            f"{self.name} | tangible | weight: {self._weight_kg:.2f} kg | logistics fee: {self._logistics_fee:.2f} | "
            f"price: {self.calculate_price():.2f} | stock: {self.stock} | active: {self.active}"
        )


class ServiceProduct(Product):
    __slots__ = ("_hours", "_complexity")

    def __init__(self, name, price, discount=0.0, stock=0, active=True, hours=1.0, complexity=1.0):
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

    def _identity_fields(self):
        return super()._identity_fields() + (self._hours, self._complexity)

    def __str__(self):
        return (
            f"{self.name} | service | hours: {self._hours:.2f} | complexity: {self._complexity:.2f} | "
            f"price: {self.calculate_price():.2f} | stock: {self.stock} | active: {self.active}"
        )