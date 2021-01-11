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
def sls(user_object, value):
    """
    Проверка длины передаваемого объекта

    user_object: Передаваемый объект (список, словарь, множество, строка и т.д.
    value: int() Длина

    Возвращает True если длина (количество элементов) равна переданной длине value
    В случае некорректного значения value, будет выдана False
    """
    try:
        length = int(value)
    except ValueError:
        return False

    return True if len(user_object) > length else False


@register.filter(name='media_folder_products')
def media_folder_products(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not string:
        string = 'products_images/default.jpg'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_blog_cover')
def media_folder_blog_cover(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    cover/placeholder-770.jpg --> /media/cover/placeholder-770.jpg
    """
    if not string:
        string = 'cover/placeholder-770.jpg'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_users')
def media_folder_users(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not string:
        string = 'users_avatars/default.jpg'

    return f'{settings.MEDIA_URL}{string}'
