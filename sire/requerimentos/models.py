from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length= 150)

class TipoRequerimento(models.Model):
    tipo = models.CharField(max_length= 150)

class Requerimento(models.Model):
    nome_requisitante = models.CharField(max_length=200)
    matricula = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoRequerimento, on_delete = models.SET_NULL, null = True)
    email = models.EmailField()
    datetime_criacao = models.DateTimeField(auto_now_add=True)
    datetime_edicao = models.DateTimeField(auto_now = True)
    curso = models.ForeignKey(Curso, on_delete = models.SET_NULL, null = True)

class Anexo(models.Model):
    datetime_criacao = models.DateTimeField(auto_now_add = True)
    datetime_edicao = models.DateTimeField(auto_now = True)
    requerimento = models.ForeignKey(Requerimento, on_delete = models.CASCADE) #Rever CASCADE
    descricao = models.CharField(max_length = 400)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Despacho(models.Model):
    requerimento = models.ForeignKey(Requerimento, on_delete=models.CASCADE) #Rever CASCADE
    conteudo = models.CharField(max_length=5000)
    datetime_criacao = models.DateTimeField(auto_now_add = True)
    datetime_edicao = models.DateTimeField(auto_now = True)
