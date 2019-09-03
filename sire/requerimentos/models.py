from django.db import models

class Requerimento(models.Model):
    nome_requisitante = models.CharField(max_length=200)
    email = models.EmailField()
    datetime_criacao = models.DateTimeField(auto_now_add=True)
    datetime_edicao = models.DateTimeField(auto_now = True)

class Anexo(models.Model):
    datetime_criacao = models.DateTimeField(auto_now_add = True)
    datetime_edicao = models.DateTimeField(auto_now = True)
    requerimento = models.ForeignKey(Requerimento, on_delete = models.CASCADE) #Rever CASCADE
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Despacho(models.Model):
    requerimento = models.ForeignKey(Requerimento, on_delete=models.CASCADE) #Rever CASCADE
    conteudo = models.CharField(max_length=2000)
    datetime_criacao = models.DateTimeField(auto_now_add = True)
    datetime_edicao = models.DateTimeField(auto_now = True)
