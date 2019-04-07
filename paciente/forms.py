from django.forms import ModelForm, DateInput, TimeInput
from .models import paciente

class pacienteForm(ModelForm):
    class Meta:
        model = paciente
        fields = '__all__'