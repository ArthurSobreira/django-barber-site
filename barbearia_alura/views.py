from django.shortcuts import render


def index(request):
    return render(request, 'barbearia_alura/index.html')


def produtos(request):
    return render(request, 'barbearia_alura/produtos.html')


def contato(request):
    return render(request, 'barbearia_alura/contato.html')
