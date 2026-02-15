from scipy.stats import norm
from utils.validators import normalize_percentage, validate_positive, validate_range

def calculate_var(mean_return, std_dev, confidence_level=0.95):

    mean_return = normalize_percentage(mean_return)
    std_dev = normalize_percentage(std_dev)

    validate_positive(std_dev, "Standard deviation")
    validate_range(confidence_level, 0, 1, "Confidence level")

    z_score = norm.ppf(1 - confidence_level)
    return -(mean_return + z_score * std_dev)
