from django import template

register = template.Library()


@register.filter(name="thousands")
def thousands_format(num):
    return round(num / 1000)
