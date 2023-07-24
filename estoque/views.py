from django.shortcuts import render
from estoque.models import Materiais
from django.contrib import messages
from django.contrib.messages import constants


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
    return render(request, 'cadastro.html')


def visualizar(request):
        materiais = Materiais.objects.all()
        materiais_get = request.GET.get()
        return render(request, 'visualiza_itens.html', {'materiais': materiais})