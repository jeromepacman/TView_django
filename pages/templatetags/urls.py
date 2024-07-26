from typing import Optional, Any, Dict

from django import template, urls

register = template.Library()


@register.simple_tag(takes_context=True)
def translate_url(context: Dict[str, Any], language: Optional[str]) -> str:
    url = context['request'].build_absolute_uri()
    return urls.translate_url(url, language)
