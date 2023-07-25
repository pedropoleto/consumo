from django.shortcuts import render, redirect
from estoque.models import Materiais, Revenda
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        quantidade = request.POST.get('quantidade')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        
        itens = Materiais(
            quantidade = quantidade,
            descricao = descricao,
            data = data,
        )
        
        itens.save()
        
        messages.add_message(request, constants.SUCCESS, 'Entrada realizada com sucesso!')
    return redirect('cadastro.html')


def visualizar(request):
        materiais = Materiais.objects.all()
        return render(request, 'visualiza_itens.html', {'materiais': materiais})
    
    
def saida(request, pk):
    revenda = Revenda.objects.all()
    materiais = Materiais.objects.get(pk=pk)
    return render(request, 'saida.html', {'materiais': materiais, 'revenda': revenda})
