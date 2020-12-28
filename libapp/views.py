from django.shortcuts import render
from libapp.models import MainMenu
from blogapp.models import Blog, BlogCategory


def main_menu_generate(menu_items):
    menu_dict = {}
    for item in menu_items:
        if not item.parent_category:
            menu_dict.update({item.hash_view: list([item.name, item.url_address], )})
        else:
            menu_dict[item.parent_category.hash_view].append([item.name, item.url_address])
    return menu_dict


def libs():
    pass


def main(request):
    nav_hash = main_menu_generate(MainMenu.objects.all())
    nav_menu = MainMenu.objects.all()
    blog_category = BlogCategory.objects.all().order_by('pk')
    blog_post = Blog.objects.all().order_by('time_publication')
    context = {
        'title': 'ООО Авиакомпания "БАРКОЛ"',
        'nav_menu': nav_menu,
        'nav_hash': nav_hash,
        'blog_category': blog_category,
        'blog_post': blog_post,
    }
    return render(request, 'libapp/index.html', context)
