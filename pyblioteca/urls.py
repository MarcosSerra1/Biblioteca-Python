from django.urls import path

from pyblioteca import views

urlpatterns = [
    path('', views.home),  # Home
    path('livros/<int:id>/', views.livros),  # livros
]
