from django.shortcuts import render, redirect, get_object_or_404
from .models import Ativo, Passivo, BalancoPatrimonial
from .forms import AtivoForm, PassivoForm

def balanco_view(request):
    # Supondo que você tenha algum jeito de classificar ou identificar circulantes e não circulantes
    ativos_circulantes = Ativo.objects.filter(circulante=True)
    passivos_circulantes = Passivo.objects.filter(circulante=True)
    ativos_nao_circulantes = Ativo.objects.filter(circulante=False)
    passivos_nao_circulantes = Passivo.objects.filter(circulante=False)

    # Cálculo dos totais
    total_ativos_circulantes = sum(ativo.valor for ativo in ativos_circulantes)
    total_passivos_circulantes = sum(passivo.valor for passivo in passivos_circulantes)
    total_ativos_nao_circulantes = sum(ativo.valor for ativo in ativos_nao_circulantes)
    total_passivos_nao_circulantes = sum(passivo.valor for passivo in passivos_nao_circulantes)

    total_ativos = total_ativos_circulantes + total_ativos_nao_circulantes
    total_passivos = total_passivos_circulantes + total_passivos_nao_circulantes
    patrimonio_liquido = total_ativos - total_passivos

    # Contexto a ser passado para o template
    context = {
        'ativos_circulantes': ativos_circulantes,
        'passivos_circulantes': passivos_circulantes,
        'ativos_nao_circulantes': ativos_nao_circulantes,
        'passivos_nao_circulantes': passivos_nao_circulantes,
        'total_ativos_circulantes': total_ativos_circulantes,
        'total_passivos_circulantes': total_passivos_circulantes,
        'total_ativos_nao_circulantes': total_ativos_nao_circulantes,
        'total_passivos_nao_circulantes': total_passivos_nao_circulantes,
        'total_ativos': total_ativos,
        'total_passivos': total_passivos,
        'patrimonio_liquido': patrimonio_liquido,
    }

    # Renderiza o template com o contexto
    return render(request, 'finance/balanco.html', context)

def add_ativo(request):
    if request.method == 'POST':
        form = AtivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('balanco')
    else:
        form = AtivoForm()
    return render(request, 'finance/add_ativo.html', {'form': form})

def add_passivo(request):
    if request.method == 'POST':
        form = PassivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('balanco')
    else:
        form = PassivoForm()
    return render(request, 'finance/add_passivo.html', {'form': form})

def edit_ativo(request, id):
    ativo = get_object_or_404(Ativo, id=id)
    if request.method == 'POST':
        form = AtivoForm(request.POST, instance=ativo)
        if form.is_valid():
            form.save()
            return redirect('balanco') # Altere para a URL apropriada
    else:
        form = AtivoForm(instance=ativo)
    return render(request, 'finance/edit_ativo.html', {'form': form})

def delete_ativo(request, id):
    ativo = get_object_or_404(Ativo, id=id)
    ativo.delete()
    return redirect('balanco') # Altere para a URL apropriada

def edit_passivo(request, id):
    passivo = get_object_or_404(Passivo, id=id)
    if request.method == 'POST':
        form = PassivoForm(request.POST, instance=passivo)
        if form.is_valid():
            form.save()
            return redirect('balanco') # Altere para a URL apropriada
    else:
        form = PassivoForm(instance=passivo)
    return render(request, 'finance/edit_passivo.html', {'form': form})

def delete_passivo(request, id):
    passivo = get_object_or_404(Passivo, id=id)
    passivo.delete()
    return redirect('balanco') # Altere para a URL apropriada
