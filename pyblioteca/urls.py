from django.urls import path

from pyblioteca.views import cadastrar_livros, editar_excluir, home, sobre

urlpatterns = [
    path('', home),  # Home
    path('editar_excluir/', editar_excluir),  # /editar_excluir/
    path('sobre/', sobre),  # /sobre/
    path('cadastrar_livros/', cadastrar_livros)  # /cadastrar_livros
]
