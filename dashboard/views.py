from django.shortcuts import render
from datetime import date
from django.http import HttpResponseRedirect
from paciente.models import paciente
from dadosFinanceiros.models import adicionarPagamento
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    pacientes = paciente.objects.all()
    pagamentosT = adicionarPagamento.objects.all()
    pagamentosD = adicionarPagamento.objects.filter(data=date.today())


    database ={
        'numeroPacientes':pacientes.count(),
        'numeroPagamentosT':pagamentosT.count(),
        'numeroPagamentosD':pagamentosD.count(),
    }
    return render(request, "dashboard.html", database)
