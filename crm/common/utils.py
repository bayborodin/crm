from datetime import datetime

from django.utils.formats import get_format


def parse_float(arg):
    """Custom parsing a string to a float."""
    if not arg:
        return 0.0

    float_string = arg
    float_string = float_string.replace(" ", "")
    float_string = float_string.replace(",", ".")

    return float(float_string)


def parse_date(date_str):
    """Parse date from string by DATE_INPUT_FORMATS of current language."""
    for item in get_format("DATE_INPUT_FORMATS"):
        try:
            return datetime.strptime(date_str, item).date()
        except (ValueError, TypeError):
            continue

    return None
