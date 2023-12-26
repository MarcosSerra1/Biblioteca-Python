from django.shortcuts import render

from pyblioteca.models import Livros
from utils.livros.factory import make_livros

# Create your views here.

def home(request):
    # return render(request,'pyblioteca/pages/home.html', context={
        # 'livros': [make_livros() for _ in range(10)],
    # })
    livros = Livros.objects.all()
    return render(request,'pyblioteca/pages/home.html', {'livros': livros})

def livros(request, id):
    # return render(request,'pyblioteca/pages/livros-view.html', context={
    #     'livro': make_livros(),
    #     'is_detail_page': True,
    # })
    livro = Livros.objects.get(id=id)
    return render(request, 'pyblioteca/pages/livros-view.html', {'livro': livro, 'is_detail_page': True})
