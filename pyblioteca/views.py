from django.http import HttpResponse
from django.shortcuts import redirect, render

from pyblioteca.models import Livros
from usuarios.models import Usuario

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        # usuario = Usuario.objects.get(id = request.session['usuario'])[0].nome
        # return HttpResponse(f' Olá {usuario}')

        livros = Livros.objects.all()
        return render(request,'pyblioteca/pages/home.html', {'livros': livros})
    else:
        return redirect('/auth/login/?status=2')

def livros(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        return render(request, 'pyblioteca/pages/livros-view.html', {'livro': livro, 'is_detail_page': True})

