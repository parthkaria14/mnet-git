def calculate_total(price_per_unit, quantity, discount_rate):
    """Return the line total, applying a discount when discount_rate is positive."""
    if discount_rate > 0:
        return price_per_unit * quantity * (1 - discount_rate)
    else:
        return price_per_unit * quantity


print(calculate_total(100, 3, 0.1))
