def _validate_name(value):
    if not isinstance(value, str):
        raise TypeError("name must be a string")
    v = value.strip()
    if not v:
        raise ValueError("name cannot be empty")
    return v

def _validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("price must be a number")
    v = float(value)
    if v < 0:
        raise ValueError("price must be >= 0")
    return v

def _validate_discount(value):
    if not isinstance(value, (int, float)):
        raise TypeError("discount must be a number")
    v = float(value)
    if v < 0 or v > 100:
        raise ValueError("discount must be between 0 and 100")
    return v

def _validate_stock(value):
    if not isinstance(value, int):
        raise TypeError("stock must be int")
    if value < 0:
        raise ValueError("stock must be >= 0")
    return value

def _validate_number(value: object, field_name: str, *, positive: bool = False, non_negative: bool = False) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"{field_name} must be numeric")
    value = float(value)
    if positive and value <= 0:
        raise ValueError(f"{field_name} must be > 0")
    if non_negative and value < 0:
        raise ValueError(f"{field_name} must be >= 0")
    return value

def _validate_int(value: object, field_name: str, *, positive: bool = False, non_negative: bool = False) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(f"{field_name} must be int")
    if positive and value <= 0:
        raise ValueError(f"{field_name} must be > 0")
    if non_negative and value < 0:
        raise ValueError(f"{field_name} must be >= 0")
    return value