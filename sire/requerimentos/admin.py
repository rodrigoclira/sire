from django.contrib import admin

from .models import Requerimento, Curso, Disciplina, UsuarioFuncao
from .models import TipoRequerimento, Anexo, Despacho, Funcao


@admin.register(Requerimento)
class RequerimentoAdmin(admin.ModelAdmin):
    list_display = ('solicitante', 'tipo', "curso", 'datetime_criacao', )
    
    
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', "curso", 'carga_horaria')

@admin.register(TipoRequerimento)
class TipoRequerimentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)


@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ("nome", )

@admin.register(UsuarioFuncao)
class UsuarioFuncao(admin.ModelAdmin):
    list_display = ('usuario', 'funcao')
admin.site.register(Despacho)

