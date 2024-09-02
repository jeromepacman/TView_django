# from typing import Optional, Any, Dict
#
# from django import template, urls
#
# register = template.Library()
#
#
# @register.simple_tag(takes_context=True)
# def translate_url(context: Dict[str, Any], language: Optional[str]) -> str:
#     url = context['request'].build_absolute_uri()
#     return urls.translate_url(url, language)
from typing import Dict, Optional

from django import template, urls

register = template.Library()


@register.simple_tag(takes_context=True)
def translate_url(context: Dict[str, any], language: Optional[str]) -> str:
    request = context['request']
    absolute_url = request.build_absolute_uri()
    return urls.translate_url(absolute_url, language)
