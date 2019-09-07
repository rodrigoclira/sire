from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nome = models.CharField(max_length = 150)
    sigla = models.CharField(max_length = 10)
    deletado = models.BooleanField("Deletado", default = False )

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length = 150)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete = models.SET_NULL, null = True)    
    deletado = models.BooleanField("Deletado", default = False )

    def __str__(self):
        return self.nome

class TipoRequerimento(models.Model):
    nome = models.CharField(max_length = 150)
    deletado = models.BooleanField("Deletado", default = False )

    def __str__(self):
        return self.nome

class Requerimento(models.Model):
    solicitante = models.CharField(max_length=200)
    matricula = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoRequerimento, on_delete = models.SET_NULL, null = True)
    email = models.EmailField()
    datetime_criacao = models.DateTimeField("Data de Criação", auto_now_add=True)
    datetime_edicao = models.DateTimeField("Data de Edição", auto_now = True)
    curso = models.ForeignKey(Curso, on_delete = models.SET_NULL, null = True)
    solicitacao = models.CharField(max_length = 2000)
    deletado = models.BooleanField("Deletado", default = False )

    def __str__(self):
        return self.tipo.nome + ' solicitado por ' + self.solicitante + ' de ' + self.curso.nome

class Anexo(models.Model):
    datetime_criacao = models.DateTimeField("Data de Criação",auto_now_add = True)
    datetime_edicao = models.DateTimeField("Data de Edição", auto_now = True)
    requerimento = models.ForeignKey(Requerimento, on_delete = models.SET_NULL, null = True)
    descricao = models.CharField(max_length = 400)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    deletado = models.BooleanField("Deletado", default = False )

class Despacho(models.Model):
    requerimento = models.ForeignKey(Requerimento, on_delete=models.SET_NULL, null = True) 
    conteudo = models.CharField(max_length=5000)
    datetime_criacao = models.DateTimeField(auto_now_add = True)
    datetime_edicao = models.DateTimeField(auto_now = True)
    despachante = models.ForeignKey(User, on_delete = models.PROTECT, related_name = 'despachante')
    proximo = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name = 'proximo')
    solicitar_alteracao = models.BooleanField("Solicitação de Alteração", default = False)
    deletado = models.BooleanField("Deletado", default = False )

class DisciplinaRequerimento(models.Model):
    disciplina = models.ForeignKey(Disciplina,  on_delete = models.SET_NULL, null = True)
    requerimento = models.ForeignKey(Requerimento, on_delete = models.SET_NULL, null = True)


class Funcao(models.Model):
    nome = models.CharField("Função", max_length=100)
    prioridade = models.IntegerField()
    def __str__(self):
        return self.nome


class UsuarioFuncao(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    funcao = models.ForeignKey(Funcao, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f"{self.funcao} - {self.usuario.first_name} {self.usuario.last_name}"