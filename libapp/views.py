from django.shortcuts import render
from libapp.models import MainMenu

# Create your views here.


def libs():
    pass


def main(request):
    nav_menu = MainMenu.objects.all()
    print(nav_menu)
    context = {
        'title': 'ООО Авиакомпания "БАРКОЛ"',
        'nav_menu': nav_menu,
    }
    return render(request, 'libapp/index.html', context)
