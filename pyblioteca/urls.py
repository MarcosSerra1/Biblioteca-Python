from django.urls import path

from pyblioteca import views

# livros:home / livros:livro
app_name = 'livros'

urlpatterns = [
    path('home/', views.home, name='home'),  # Home pagina vitrine
    path('livros/<int:id>/', views.livros, name='livro'),  # livros
]
