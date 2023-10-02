from django import forms



class QuestionForm(forms.Form):
    question = forms.CharField(label="Digite a pergunta", max_length=250)
