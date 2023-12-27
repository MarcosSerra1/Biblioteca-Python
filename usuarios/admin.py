from django.contrib import admin

from .models import *


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'sobrenome', 'email', 'senha')
