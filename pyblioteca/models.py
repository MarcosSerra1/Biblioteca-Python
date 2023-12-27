from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=200)


    class Meta():
        verbose_name = 'Autore'


    def __str__(self):
        return self.nome


class Genero(models.Model):
    genero = models.CharField(max_length=200)

    def __str__(self):
        return self.genero


class Livros(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    slug = models.SlugField(max_length=100, null=True)
    tempo_de_leitura = models.CharField(max_length=100)
    quantidade_de_livros = models.IntegerField()
    capitulos = models.IntegerField()
    data_de_lancamento = models.DateField()
    esta_emprestado = models.BooleanField(default=False)
    capa = models.ImageField(upload_to='livros/capas/%Y/%m/%d/')
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)


    class Meta():
        verbose_name = 'Livro'


    def __str__(self):
        return self.titulo
