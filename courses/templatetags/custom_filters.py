from django import template
register = template.Library()

@register.filter
def percentage(part, total):
    try:
        return (part / total) * 100
    except:
        return 0
