from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='sls')
def sls(user_list, start):
    """
    Срез списка, с заданной позиции
    """
    return user_list[int(start):]


@register.filter(name='len')
def sls(user_list, value):
    """
    Срез списка, с заданной позиции
    """
    return True if len(user_list) > int(value) else False
