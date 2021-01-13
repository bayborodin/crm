from django import template

register = template.Library()


@register.filter(name="thousands")
def thousands_format(num):
    """Format thousands numbers representation."""
    num = round(num / 1000)
    return f"{num:,}".replace(",", " ")
