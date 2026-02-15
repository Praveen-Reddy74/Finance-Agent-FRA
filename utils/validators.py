def normalize_percentage(value):
    """
    Converts percentage inputs like 5 or 20 into decimal form (0.05, 0.20).
    If already decimal (<=1), returns unchanged.
    """
    if value > 1:
        return value / 100
    return value


def validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be positive.")


def validate_range(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        raise ValueError(f"{name} must be between {min_val} and {max_val}.")
