from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import adicionarPagamento
from .forms import pagamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def createPagamento(request):
    form = pagamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/pagamento/adicionar/')
    
    return render(request, "adicionarPagamento.html", {'form':form})


@login_required
def searchPagamento(request):
    nome = request.GET.get('search', None)

    if nome:
        pagamentos = adicionarPagamento.objects.filter(nomePaciente__Nome__contains=nome)

    else:
        pagamentos = adicionarPagamento.objects.all()

    dataBase = {
        'pagamentos': pagamentos
    }
    return render(request, 'buscarPagamentos.html', dataBase)


@login_required
def delPagamento(request, pk):
    adicionarPagamento.objects.filter(id=pk).delete()

    return HttpResponseRedirect('/pagamento/buscar/')

@login_required
def editPagamento(request,pk):
    pagamento = adicionarPagamento.objects.get(id=pk)

    if request.method == "POST":
        form = pagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect("/pagamento/buscar/")
    else:
        form = pagamentoForm(instance=pagamento)

    return render(request, 'editarPagamentos.html', {'form':form})