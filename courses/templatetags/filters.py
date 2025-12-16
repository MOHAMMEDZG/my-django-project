from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    if not url:
        return ""

    # إذا غير ID
    if re.match(r'^[\w-]{11}$', url):
        return f"https://www.youtube.com/embed/{url}"

    # watch?v=
    match = re.search(r'v=([\w-]{11})', url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"

    # youtu.be
    match = re.search(r'youtu\.be/([\w-]{11})', url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"

    return ""
