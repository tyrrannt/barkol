from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView

from blogapp.forms import CreateNewPostForm
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


class CreateNewPost(CreateView):
    context = {}
    model = Blog
    template_name = 'blogapp/create.html'
    success_url = reverse_lazy('blog:index')
    form_class = CreateNewPostForm

    @method_decorator(user_passes_test(lambda u: u.is_active))
    def dispatch(self, request, *args, **kwargs):
        return super(CreateNewPost, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateNewPost, self).get_context_data(**kwargs)
        context['title'] = title = 'Создание нового поста'
        return context
