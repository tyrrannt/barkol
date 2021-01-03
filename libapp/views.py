from django.shortcuts import render
from libapp.models import MainMenu
from blogapp.models import Blog, BlogCategory
from authapp.models import Counteragent
from edo.utilities import main_menu_generate, footer_info_generator




def libs():
    pass


def main(request):
    blog_category = BlogCategory.objects.all().order_by('pk')
    blog_post = Blog.objects.all().order_by('time_publication')
    context = {
        'title': 'ООО Авиакомпания "БАРКОЛ" - БИБЛИОТЕКА',
        'blog_category': blog_category,
        'blog_post': blog_post,
    }
    context.update(main_menu_generate(MainMenu.objects.all()))
    try:
        context.update(footer_info_generator(Counteragent.objects.get(base_counteragent=True)))
    except Exception:
        pass
    return render(request, 'libapp/index.html', context)
