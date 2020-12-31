from django.shortcuts import render
from blogapp.models import Blog, BlogCategory
from libapp.models import MainMenu
from edo.utilities import main_menu_generate


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
    return render(request, 'blogapp/index.html', context)
