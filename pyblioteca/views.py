from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'pyblioteca/pages/home.html')


def livros(request, id):
    return render(request,'pyblioteca/pages/livros-view.html')
