from django import forms
from .models import Curso, Requerimento, TipoRequerimento

class RequerimentoForm(forms.ModelForm):
    solicitante = forms.CharField(label="Nome")
    matricula = forms.CharField(label = "Matrícula")
    email = forms.EmailField(label = "E-mail")

    choices_curso = [(curso.sigla, curso.nome) for curso in Curso.objects.all()]    
    choices_curso.insert(0, ("None", "Selecionar..."))
    curso = forms.ChoiceField(label="Curso", widget=forms.Select, choices=choices_curso)
    
    choices_tipo = [(tipo.pk, tipo.nome) for tipo in TipoRequerimento.objects.all()]    
    choices_tipo.insert(0, (-1, "Selecionar..."))    
    tipo = forms.ChoiceField(label="Tipo", widget=forms.Select, choices=choices_tipo)
    
    solicitacao = forms.CharField(label = "Solicitação", widget=forms.Textarea(attrs={"rows":4,}))
    upload = forms.FileField(required=False)


    solicitante.widget.attrs.update({'class': 'form-control'})
    matricula.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    curso.widget.attrs.update({'class': 'form-control'})
    tipo.widget.attrs.update({'class': 'form-control'})
    solicitacao.widget.attrs.update({'class': 'form-control'})

        
    class Meta: 
        model = Requerimento
        fields = ("solicitante", "matricula", "email", "solicitacao") # colocar o upload
    
    