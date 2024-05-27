from django import template

register = template.Library()

@register.filter(name='remove_quotes')
def remove_quotes(value):
    if isinstance(value, str):
        return value.replace('"', '').replace("'", '')
    return value