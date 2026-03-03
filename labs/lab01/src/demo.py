from model import Product, CartItem, Customer, Order, Payment


def separator(title):
    print("\n" + "=" * 15, title, "=" * 15)


def main():
    separator("АТРИБУТ КЛАССА")
    print("Название магазина:", Product.shop_name)

    # СЦЕНАРИЙ 1 — УСПЕШНЫЙ ЗАКАЗ

    separator("СЦЕНАРИЙ 1 — УСПЕШНАЯ ПОКУПКА")

    laptop = Product("Laptop", 100000.0, 5, 10)
    mouse = Product("Mouse", 1500.0, 10)

    print(laptop)
    print(mouse)

    customer = Customer("Иван Петров", "ivan@mail.ru", "Москва, ул. Пушкина 10")
    print(customer)

    item1 = CartItem(laptop, 1)
    item2 = CartItem(mouse, 2)

    order = Order(customer)
    order.add_item(item1)
    order.add_item(item2)

    print("\nЗаказ до оплаты:")
    print(order)

    payment = Payment(order.total(), "card")
    order.pay(payment)

    print("\nЗаказ после оплаты:")
    print(order)

    order.ship()
    print("\nПосле отправки:")
    print("Статус:", order.status)


    # СЦЕНАРИЙ 2 — НЕУДАЧНАЯ ОПЛАТА

    separator("СЦЕНАРИЙ 2 — НЕХВАТКА СРЕДСТВ")

    keyboard = Product("Keyboard", 5000.0, 3)
    item = CartItem(keyboard, 2)

    order2 = Order(customer, items=[item])

    bad_payment = Payment(1000.0, "card")

    try:
        order2.pay(bad_payment)
    except Exception as e:
        print("Ошибка оплаты:", e)

    print("Статус заказа:", order2.status)


    # СЦЕНАРИЙ 3 — ОТМЕНА И ВОЗВРАТ

    separator("СЦЕНАРИЙ 3 — ОТМЕНА С ВОЗВРАТОМ")

    monitor = Product("Monitor", 20000.0, 2)
    item_m = CartItem(monitor, 2)

    order3 = Order(customer, items=[item_m])
    payment3 = Payment(order3.total(), "paypal")
    order3.pay(payment3)

    print("До отмены:")
    print("Статус заказа:", order3.status)
    print("Статус платежа:", order3.payment.status)
    print("Остаток мониторов:", monitor.stock)

    order3.cancel()

    print("\nПосле отмены:")
    print("Статус заказа:", order3.status)
    print("Статус платежа:", order3.payment.status)
    print("Остаток мониторов восстановлен:", monitor.stock)

    # СЦЕНАРИЙ 4 — АВТО-ДЕАКТИВАЦИЯ

    separator("СЦЕНАРИЙ 4 — АВТО-ДЕАКТИВАЦИЯ ТОВАРА")

    phone = Product("Phone", 30000.0, 1)
    print(phone)

    phone.sell(1)
    print("После продажи последнего экземпляра:")
    print(phone)

    try:
        phone.sell(1)
    except Exception as e:
        print("Ошибка продажи:", e)


    # СЦЕНАРИЙ 5 — SETTER + ВАЛИДАЦИЯ

    separator("СЦЕНАРИЙ 5 — ПРОВЕРКА SETTER")

    try:
        laptop.discount = 50
        print("Новая цена ноутбука:", laptop.get_final_price())
    except Exception as e:
        print("Ошибка:", e)

    try:
        laptop.price = -100
    except Exception as e:
        print("Ошибка изменения цены:", e)

    try:
        customer.email = "invalid-email"
    except Exception as e:
        print("Ошибка изменения email:", e)

    # СЦЕНАРИЙ 6 — НЕВЕРНОЕ СОЗДАНИЕ

    separator("СЦЕНАРИЙ 6 — НЕКОРРЕКТНОЕ СОЗДАНИЕ")

    try:
        Product("", -100, -5, 200)
    except Exception as e:
        print("Ошибка при создании продукта:", e)

    try:
        Customer("A", "bad", "")
    except Exception as e:
        print("Ошибка при создании клиента:", e)

    try:
        Payment(-500, "crypto")
    except Exception as e:
        print("Ошибка при создании платежа:", e)

    # СЦЕНАРИЙ 7 — СРАВНЕНИЕ ОБЪЕКТОВ

    separator("СЦЕНАРИЙ 7 — СРАВНЕНИЕ")

    p1 = Product("Laptop", 100000.0, 1)
    p2 = Product("Laptop", 100000.0, 10)
    p3 = Product("Laptop", 120000.0, 1)

    print("p1 == p2 ?", p1 == p2)  # True
    print("p1 == p3 ?", p1 == p3)  # False

    # СЦЕНАРИЙ 8 — LOYALTY POINTS
    
    separator("СЦЕНАРИЙ 8 — БОНУСНЫЕ БАЛЛЫ")

    print("Очки до:", customer.loyalty_points)
    customer.add_points(100)
    print("Очки после начисления:", customer.loyalty_points)

    try:
        customer.spend_points(200)
    except Exception as e:
        print("Ошибка списания:", e)

    customer.spend_points(50)
    print("Очки после списания:", customer.loyalty_points)


if __name__ == "__main__":
    main()