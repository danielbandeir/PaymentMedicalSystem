from django.db import models
from paciente.models import paciente

class adicionarPagamento(models.Model):
    nomePaciente = models.ForeignKey(paciente, blank=True, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()
    meioDePagamento = models.CharField(max_length=60)
    valor = models.CharField(max_length=80)

    def __str__(self):
        return '{} - {} - {}'.format(self.nomePaciente, self.data, self.valor)
