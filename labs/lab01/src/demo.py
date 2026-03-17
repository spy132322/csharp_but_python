from model import Product

print("=== СЦЕНАРИЙ 1: СОЗДАНИЕ И СРАВНЕНИЕ ===")
p1 = Product("Laptop", 1000, discount=10, stock=3)
p2 = Product("Laptop", 1000, discount=10, stock=3)

print(p1)
print(repr(p1))
print("equal:", p1 == p2)

print("\n=== СЦЕНАРИЙ 2: ВАЛИДАЦИЯ ===")
try:
    bad = Product("", -100, discount=200, stock=-5)
except Exception as e:
    print("error:", type(e).__name__, e)

try:
    p1.discount = 150
except Exception as e:
    print("setter error:", type(e).__name__, e)

print("\n=== СЦЕНАРИЙ 3: ПОКУПКА ===")
print("before:", p1)
p1.purchase(1)
print("after:", p1)

try:
    p1.purchase(10)
except Exception as e:
    print("purchase error:", type(e).__name__, e)

print("\n=== СЦЕНАРИЙ 4: СОСТОЯНИЕ ===")
p3 = Product("Phone", 500, stock=1, active=False)

try:
    p3.purchase(1)
except Exception as e:
    print("inactive error:", type(e).__name__, e)

p3.activate()
print("activated:", p3)
print("purchase:", p3.purchase(1))

print("\n=== СЦЕНАРИЙ 5: ИЗМЕНЕНИЕ ДАННЫХ ===")
p1.price = 1200
p1.discount = 20
p1.restock(5)

print("updated:", p1)

print("\n=== СЦЕНАРИЙ 6: ЦЕНА ===")
print("with discount:", p1.price_after_discount())
print("with tax:", p1.price_with_tax())

print("\n=== СЦЕНАРИЙ 7: АТРИБУТ КЛАССА ===")
print("tax via class:", Product.TAX_RATE)
print("tax via object:", p1.TAX_RATE)