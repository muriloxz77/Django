from django import forms
from .models import TIPOS_QUARTOS


class CheckinForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=20)
    sobrenome = forms.CharField(label="Sobrenome", max_length=20)
    email = forms.EmailField(label="Email", max_length=50)
    tipo_quarto = forms.ChoiceField(label="Tipo de quarto", choices=TIPOS_QUARTOS)
    data_reserva = forms.DateField(label="Data de reserva")
