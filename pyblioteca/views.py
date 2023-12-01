from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'pyblioteca/pages/home.html')


def editar_excluir(request):
    return HttpResponse('Editar ou Excluir um Livro')


def sobre(request):
    return HttpResponse('Sobre Nós')


def cadastrar_livros(request):
    return render(request, 'pyblioteca/pages/formulario.html')
