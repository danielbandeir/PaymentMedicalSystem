from django.forms import ModelForm, DateInput, TimeInput,DateField, TextInput
from .models import adicionarPagamento
from paciente.models import paciente

class pagamentoForm(ModelForm):
    class Meta:
        model = adicionarPagamento
        fields = '__all__'
        widgets = {
            'data': DateInput(attrs={'class': 'datepicker'}),
            'hora': TimeInput(attrs={'type': 'time'}),
            'descricao': TextInput(attrs={'class': 'materialize-textarea'}),
        }