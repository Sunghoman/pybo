from django import template
import markdown
from django.utils.safestring import mark_safe
register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

@ register.filter()
def mark(value):
    extensions = ["nl2br","fenced_code"] # 마크다운의 소스코드 표현 및 줄바꿈 문자 <br>
    return mark_safe(markdown.markdown(value, extensions=extensions))