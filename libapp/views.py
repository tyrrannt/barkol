from django.shortcuts import render

# Create your views here.


def libs():
    pass


def main(request):
    context = {
        'title': 'ООО Авиакомпания "БАРКОЛ"',
    }
    return render(request, 'libapp/index.html', context)
