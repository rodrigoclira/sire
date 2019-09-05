from django.contrib import admin

from .models import *


@admin.register(Requerimento)
class RequerimentoAdmin(admin.ModelAdmin):
    list_display = ('solicitante', 'tipo', 'curso', 'datetime_criacao', )

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', "curso", 'carga_horaria')

@admin.register(TipoRequerimento)
class TipoRequerimentoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)


admin.site.register(Despacho)

