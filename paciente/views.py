from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import pacienteForm
from .models import paciente
from django.contrib.auth.decorators import login_required


@login_required
def createPaciente(request):
    form = pacienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/paciente/criar/')

    return render(request, 'criarPaciente.html', {'form' : form})

@login_required
def buscarPaciente(request):
    nome = request.GET.get('search', None)

    if nome:
        pacientes = paciente.objects.filter(Nome__contains=nome)

    else:
        pacientes = paciente.objects.all()

    dataBase = {
        'pacientes': pacientes
    }
    return render(request, 'buscarPaciente.html', dataBase)


@login_required
def deletarPacie(request, pk):
    paciente.objects.filter(id=pk).delete()

    return HttpResponseRedirect('/paciente/buscar/')

@login_required
def verFicha(request, pk):
    pessoa = paciente.objects.filter(id=pk)
    pessoaItem = paciente.objects.get(id=pk)


    dataBase = {
        'pessoas':pessoa
    }

    return render(request, 'verFicha.html', dataBase)

@login_required
def editarPacie(request,pk):

    pessoa = paciente.objects.get(id=pk)

    if request.method == "POST":
        form = pacienteForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect("/paciente/buscar/")
    else:
        form = pacienteForm(instance=pessoa)


    return render(request, 'editarPacient.html', {'form':form})