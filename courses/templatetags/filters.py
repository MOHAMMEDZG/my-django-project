import re
from django import template

register = template.Library()

@register.filter
def youtube_embed(url):
    if not url:
        return ""

    # Extracting code from all types of links
    patterns = [
        r"youtube\.com/watch\?v=([^&]+)",
        r"youtu\.be/([^?&]+)",
        r"youtube\.com/embed/([^?&]+)",
        r"youtube\.com/shorts/([^?&]+)"
    ]

    video_id = None
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            break

    if not video_id:
        return ""

    # build link embed
    return f"https://www.youtube.com/embed/{video_id}"
