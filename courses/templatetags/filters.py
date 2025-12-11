from django import template
import re

register = template.Library()

@register.filter
def youtube_embed(url):
    """
    Converts normal YouTube URLs to embed URLs.
    Supports:
    - https://www.youtube.com/watch?v=ID
    - https://youtu.be/ID
    - shorts
    """
    if "embed" in url:
        return url

    # youtu.be link
    match = re.match(r'https://youtu\.be/(.+)', url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"

    # normal watch?v=
    match = re.search(r'v=([^&]+)', url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"

    # shorts
    match = re.match(r'https://www.youtube.com/shorts/(.+)', url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"

    return url
