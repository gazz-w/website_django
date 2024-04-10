from django.shortcuts import render


def index(request):
    return render(request, 'landing_page/index.html')


def imagem(request):
    return render(request, 'landing_page/imagem.html')
