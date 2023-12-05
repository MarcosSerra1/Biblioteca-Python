from django.urls import path

from pyblioteca import views

# livros:home / livros:livro
app_name = 'livros'

urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('livros/<int:id>/', views.livros, name='livro'),  # livros
]
