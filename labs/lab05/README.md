# ЛР-5 — Функции как аргументы. Стратегии и делегаты

## Реализованные классы и методы

### ProductCatalog

- `sort_by(key_func, reverse=False)`  
  Сортировка коллекции по переданной функции.

- `sort_by_comparable(reverse=False)`  
  Сортировка с использованием `compare_to()`.

- `filter_by(predicate)`  
  Фильтрация коллекции по условию.

- `apply(func)`  
  Применяет функцию ко всем элементам коллекции.

- `get_printable()`  
  Возвращает элементы, поддерживающие строковое представление.

### Product и наследники

- `calculate_price()`  
  Рассчитывает итоговую цену объекта.

- `price_after_discount()`  
  Возвращает цену с учётом скидки.

- `compare_to(other)`  
  Сравнение объектов по цене.

- `to_string()`  
  Возвращает строковое представление.

### LiquidProduct
- `calculate_price()` — цена зависит от объёма и доп. стоимости

### TangibleProduct
- `calculate_price()` — цена зависит от веса и логистики

### ServiceProduct
- `calculate_price()` — цена зависит от времени и сложности

## Функции и стратегии

### Сортировка
- `by_name` — по имени  
- `by_price` — по цене  
- `by_stock` — по количеству  
- `by_type_then_price` — по типу и цене  

### Фильтрация
- `is_active` — активные  
- `is_in_stock` — есть в наличии  
- `is_type(type)` — фильтр по типу  
- `is_expensive(min_price)` — фильтр по цене  

### Преобразование
- `apply_discount(percent)`  
  Возвращает функцию для применения скидки


### Callable-стратегии
- `DiscountStrategy` — применяет скидку  
- `ActivateStrategy` — активирует объект  


## demo.py

### Сценарий 1 — цепочка операций

Последовательное применение операций к коллекции:


filter → sort → apply


- фильтрация: `is_in_stock`
- сортировка: `by_price`
- применение: `apply_discount`

![Scenario 1](/labs/lab05/images/Screenshot_20260505_150015.png)


### Сценарий 2 — замена стратегии

Сравнение разных стратегий без изменения кода коллекции:

- сортировка через функцию `by_price`
- сортировка через `compare_to()` (`sort_by_comparable`)
- применение скидки:
  - через функцию `apply_discount`
  - через callable-объект `DiscountStrategy`

![Scenario 2](/labs/lab05/images/Screenshot_20260505_150025.png)

---

### Сценарий 3 — функции высшего порядка

Использование `map`, `filter` и фабрик функций:

- `map` — получение списка имён
- `filter` — фильтрация через `is_expensive`
- фабрика — `is_type(ServiceProduct)`

![Scenario 3](/labs/lab05/images/Screenshot_20260505_150033.png)
