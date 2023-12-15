from django.contrib import admin

from .models import *


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...


class GeneroAdmin(admin.ModelAdmin):
    ...


@admin.register(Livros)
class LivroAdmin(admin.ModelAdmin):
    ...


admin.site.register(Genero, GeneroAdmin)
