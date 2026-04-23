from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros'
    })
def hola_mundo(request):
    return render(request, 'mainapp/hola_mundo.html')
