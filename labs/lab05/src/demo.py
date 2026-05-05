from models import Product, LiquidProduct, TangibleProduct, ServiceProduct
from collection import ProductCatalog
import strategies as s


def show(title, data):
    print(f"\n--- {title} ---")
    print(data)


def main():
    catalog = ProductCatalog([
        Product("Base", 100, 10, 5),
        LiquidProduct("Water", 2, 0, 100, volume_liters=2),
        TangibleProduct("Laptop", 1500, 5, 3, weight_kg=2, logistics_fee=10),
        ServiceProduct("Repair", 50, 0, 10, hours=2, complexity=2),
        Product("Phone", 800, 0, 0),
    ])

    show("Original", catalog)

    # Сценарий 1 — цепочка операций
    chain = (
        catalog
        .filter_by(s.is_in_stock)
        .sort_by(s.by_price)
        .apply(s.apply_discount(10))
    )
    show("Scenario 1: filter → sort → apply", chain)

    # Сценарий 2 — замена стратегии
    show("Sort by function", catalog.sort_by(s.by_price))
    show("Sort by comparable", catalog.sort_by_comparable())

    show("Discount via function", catalog.apply(s.apply_discount(15)))
    show("Discount via callable", catalog.apply(s.DiscountStrategy(15)))

    # Сценарий 3 — функции высшего порядка
    names = list(map(lambda x: x.name, catalog))
    show("Map names", names)

    expensive = list(filter(s.is_expensive(100), catalog))
    show("Filter expensive", [str(x) for x in expensive])

    services = catalog.filter_by(s.is_type(ServiceProduct))
    show("Filter services", services)


if __name__ == "__main__":
    main()
