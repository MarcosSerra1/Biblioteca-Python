from django.db import models


# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=200)

class Genero(models.Model):
    genero = models.CharField(max_length=200)

class Livros(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tempo_de_leitura = models.IntegerField()
    quantidade_de_livros = models.IntegerField()
    capitulos = models.IntegerField()
    lancado_em = models.DateField()
    esta_emprestado = models.BooleanField(default=False)
    capa = models.ImageField(upload_to='livros/capas/%Y/%m/%d/', null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
