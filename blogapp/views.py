from django.shortcuts import render
from blogapp.models import Blog, BlogCategory
from libapp.models import MainMenu
from authapp.models import Counteragent
from edo.utilities import main_menu_generate, footer_info_generator

# Create your views here.

def index(request):
    blog_category = BlogCategory.objects.all().order_by('pk')
    blog_post = Blog.objects.all().order_by('time_publication')
    context = {
        'title': 'ООО Авиакомпания "БАРКОЛ" - БЛОГ',
        'blog_category': blog_category,
        'blog_post': blog_post,
    }
    context.update(main_menu_generate(MainMenu.objects.all()))
    context.update(footer_info_generator(Counteragent.objects.get(base_counteragent=True)))
    return render(request, 'blogapp/index.html', context)
