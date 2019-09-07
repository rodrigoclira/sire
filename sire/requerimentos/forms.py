from django import forms
from .models import Curso

class RequerimentoForm(forms.Form):
    nome = forms.CharField()
    matricula = forms.CharField(label = "Matrícula")
    email = forms.EmailField(label = "E-mail")
    choices = [(curso.sigla, curso.nome) for curso in Curso.objects.all()]
    choices.insert(0, ("None", "Selecionar... "))
    curso = forms.ChoiceField(label="Curso", widget=forms.Select, choices=choices)
    solicitacao = forms.CharField(label = "Solicitação", widget=forms.Textarea(attrs={"rows":4,}))
    upload = forms.FileField(required=False)


    nome.widget.attrs.update({'class': 'form-control'})
    matricula.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    curso.widget.attrs.update({'class': 'form-control'})
    solicitacao.widget.attrs.update({'class': 'form-control'})
    
    