from django.shortcuts import render, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from authapp.forms import UserLoginForm
from authapp.forms import UserRegisterForm
from authapp.forms import UserEditForm
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from authapp.models import Person
from libapp.models import MainMenu
from edo.utilities import main_menu_generate, weather, groups
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


class UserProfile(DetailView):
    context = {}
    model = Person
    template_name = 'authapp/users/user_profile.html'
    success_url = reverse_lazy('authapp:profile')
    form_class = UserEditForm


    @method_decorator(user_passes_test(lambda u: u.is_active))
    def dispatch(self, request, *args, **kwargs):
        return super(UserProfile, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['title'] = title = 'редактирование'
        context.update(weather('524901'))
        context.update(groups())
        return context

class AdminUsersActive(DeleteView):
    model = Person
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

def login(request):
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    context = {'login_form': login_form}
    context.update(main_menu_generate(MainMenu.objects.all()))
    return render(request, 'libapp/index.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()


    context = {'title': title, 'register_form': register_form}
    context.update(main_menu_generate(MainMenu.objects.all()))
    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'Редактирование профиля'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        edit_form = UserEditForm(instance=request.user)

    context = {'title': title, 'edit_form': edit_form}
    context.update(main_menu_generate(MainMenu.objects.all()))
    return render(request, 'authapp/edit.html', context)
