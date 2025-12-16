from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(value):
    if not value:
        return ""

    value = value.strip()

    # إذا عطا غير ID
    if re.fullmatch(r'[\w-]{11}', value):
        return f"https://www.youtube.com/embed/{value}"

    # watch?v=
    match = re.search(r'v=([\w-]{11})', value)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"

    # youtu.be
    match = re.search(r'youtu\.be/([\w-]{11})', value)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"

    return ""
