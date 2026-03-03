import uuid
from typing import List, Optional
from validators import (
    validate_name,
    validate_price,
    validate_stock,
    validate_discount,
    validate_quantity,
    validate_email,
    validate_address,
    validate_payment_method,
    validate_positive_amount,
)


class Product:
    shop_name = "Python Store"

    def __init__(self, name: str, price: float, stock: int, discount: float = 0.0):
        validate_name(name)
        validate_price(price)
        validate_stock(stock)
        validate_discount(discount)

        self._name = name
        self._price = float(price)
        self._stock = stock
        self._discount = float(discount)
        self._is_active = True

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        validate_price(value)
        self._price = float(value)

    @property
    def stock(self):
        return self._stock

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        validate_discount(value)
        self._discount = float(value)

    @property
    def is_active(self):
        return self._is_active

    def get_final_price(self):
        return self._price * (1 - self._discount / 100)

    def sell(self, quantity: int):
        if not self._is_active:
            raise RuntimeError("Товар снят с продажи")
        validate_quantity(quantity)
        if quantity > self._stock:
            raise ValueError("Недостаточно товара на складе")
        self._stock -= quantity
        if self._stock == 0:
            self.deactivate()

    def restock(self, amount: int):
        if not isinstance(amount, int):
            raise TypeError("Пополнение должно быть целым числом")
        if amount <= 0:
            raise ValueError("Пополнение должно быть положительным")
        self._stock += amount
        if self._stock > 0:
            self._is_active = True

    def deactivate(self):
        self._is_active = False

    def activate(self):
        if self._stock == 0:
            raise RuntimeError("Нельзя активировать товар с нулевым остатком")
        self._is_active = True

    def __str__(self):
        status = "Активен" if self._is_active else "Снят"
        return (
            f"{self._name} | Цена: {self.get_final_price():.2f} ₽ "
            f"(скидка {self._discount:.1f}%) | Остаток: {self._stock} | {status}"
        )

    def __repr__(self):
        return (
            f"Product(name={self._name!r}, price={self._price!r}, "
            f"stock={self._stock!r}, discount={self._discount!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self._name == other._name and self._price == other._price


class CartItem:
    """Позиция в корзине: товар + количество"""

    def __init__(self, product: Product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError("product должен быть экземпляром Product")
        validate_quantity(quantity)
        if not product.is_active:
            raise RuntimeError("Нельзя добавить неактивный товар в корзину")

        self._product = product
        self._quantity = quantity

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        validate_quantity(value)
        if value > self._product.stock:
            raise ValueError("Количество в CartItem не может превышать остаток на складе")
        self._quantity = value

    def subtotal(self) -> float:
        return self._product.get_final_price() * self._quantity

    def __str__(self):
        return f"{self._product.name} x {self._quantity} = {self.subtotal():.2f} ₽"

    def __repr__(self):
        return f"CartItem(product={self._product!r}, quantity={self._quantity!r})"

    def __eq__(self, other):
        if not isinstance(other, CartItem):
            return False
        return self._product == other._product and self._quantity == other._quantity


class Customer:
    """Класс покупателя"""

    def __init__(self, name: str, email: str, address: str):
        validate_name(name)
        validate_email(email)
        validate_address(address)

        self._name = name
        self._email = email.strip()
        self._address = address.strip()
        self._loyalty_points = 0
        self._customer_id = str(uuid.uuid4())

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        validate_email(value)
        self._email = value.strip()

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: str):
        validate_address(value)
        self._address = value.strip()

    @property
    def loyalty_points(self) -> int:
        return self._loyalty_points

    @property
    def customer_id(self) -> str:
        return self._customer_id

    def add_points(self, points: int):
        if not isinstance(points, int):
            raise TypeError("Очки должны быть целым числом")
        if points <= 0:
            raise ValueError("Добавляемые очки должны быть положительными")
        self._loyalty_points += points

    def spend_points(self, points: int):
        if not isinstance(points, int):
            raise TypeError("Очки должны быть целым числом")
        if points <= 0:
            raise ValueError("Снимаемые очки должны быть положительными")
        if points > self._loyalty_points:
            raise ValueError("Недостаточно очков")
        self._loyalty_points -= points

    def __str__(self):
        return f"{self._name} <{self._email}> | Адрес: {self._address} | Очки: {self._loyalty_points}"

    def __repr__(self):
        return f"Customer(name={self._name!r}, email={self._email!r}, address={self._address!r})"

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return False
        return self._customer_id == other._customer_id


class Payment:
    """Платеж за заказ"""

    def __init__(self, amount: float, method: str):
        validate_positive_amount(amount)
        validate_payment_method(method)

        self._amount = float(amount)
        self._method = method.lower()
        self._status = "pending"
        self._transaction_id = str(uuid.uuid4())

    @property
    def amount(self):
        return self._amount

    @property
    def method(self):
        return self._method

    @property
    def status(self):
        return self._status

    @property
    def transaction_id(self):
        return self._transaction_id

    def process(self, required_amount: float):
        """Простая имитация обработки платежа."""
        validate_positive_amount(required_amount)
        if self._amount < required_amount:
            self._status = "failed"
            raise RuntimeError("Оплата не покрывает сумму заказа")
        self._status = "completed"

    def refund(self):
        if self._status != "completed":
            raise RuntimeError("Можно вернуть только завершенный платеж")
        self._status = "refunded"

    def __str__(self):
        return f"Payment {self._transaction_id} | {self._amount:.2f} ₽ | {self._method} | {self._status}"

    def __repr__(self):
        return f"Payment(amount={self._amount!r}, method={self._method!r}, status={self._status!r})"


class Order:
    """Заказ: набор CartItem, привязан к Customer"""

    def __init__(self, customer: Customer, items: List[CartItem] = None, shipping_address: str = None):
        if not isinstance(customer, Customer):
            raise TypeError("customer должен быть экземпляром Customer")
        self._order_id = str(uuid.uuid4())
        self._customer = customer
        self._items: List[CartItem] = items.copy() if items else []
        self._status = "created"
        self._payment: Optional['Payment'] = None
        self._shipping_address = shipping_address.strip() if shipping_address else customer.address

    @property
    def order_id(self):
        return self._order_id

    @property
    def customer(self):
        return self._customer

    @property
    def items(self):
        return self._items.copy()

    @property
    def status(self):
        return self._status

    @property
    def payment(self):
        return self._payment

    @property
    def shipping_address(self):
        return self._shipping_address

    def add_item(self, cart_item: CartItem):
        if self._status != "created":
            raise RuntimeError("Нельзя изменять заказ в текущем статусе")
        if not isinstance(cart_item, CartItem):
            raise TypeError("Нужно передать CartItem")
        if cart_item.quantity > cart_item.product.stock:
            raise ValueError("Недостаточно товара для добавления в заказ")
        self._items.append(cart_item)

    def remove_item(self, cart_item: CartItem):
        if self._status != "created":
            raise RuntimeError("Нельзя изменять заказ в текущем статусе")
        self._items.remove(cart_item)

    def total(self) -> float:
        return sum(item.subtotal() for item in self._items)

    def pay(self, payment: Payment):
        if self._status != "created":
            raise RuntimeError("Оплата возможна только для созданного заказа")
        if not isinstance(payment, Payment):
            raise TypeError("payment должен быть экземпляром Payment")
        payment.process(self.total())
        self._payment = payment
        self._status = "paid"
        for item in self._items:
            item.product.sell(item.quantity)

    def ship(self):
        if self._status != "paid":
            raise RuntimeError("Нельзя отправить заказ, пока он не оплачен")
        self._status = "shipped"

    def cancel(self):
        if self._status == "shipped":
            raise RuntimeError("Нельзя отменить уже отправленный заказ")
        if self._status == "paid":
            if self._payment and self._payment.status == "completed":
                self._payment.refund()
            for item in self._items:
                item.product.restock(item.quantity)
        self._status = "cancelled"

    def __str__(self):
        lines = [
            f"Order {self._order_id}",
            f"Customer: {self._customer.name} ({self._customer.email})",
            f"Status: {self._status}",
            "Items:"
        ]
        for it in self._items:
            lines.append(f"  - {it}")
        lines.append(f"Total: {self.total():.2f} ₽")
        if self._payment:
            lines.append(f"Payment: {self._payment}")
        return "\n".join(lines)

    def __repr__(self):
        return f"Order(order_id={self._order_id!r}, customer={self._customer!r}, items={self._items!r}, status={self._status!r})"

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return self._order_id == other._order_id