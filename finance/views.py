from django.shortcuts import render, redirect, get_object_or_404
from .models import Ativo, Passivo, DemonstracaoResultado
from .forms import AtivoForm, PassivoForm, DemostracaoResultadoForm

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

def add_demonstracao_resultado(request):
    if request.method == "POST":
        form = DemostracaoResultadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('demonstracao_resultados') # Redireciona para a tabela após adição
    else:
        form = DemostracaoResultadoForm()

    return render(request, 'finance/add_demonstracao_resultado.html', {'form': form})

def edit_demonstracao_resultado(request, pk):
    resultado = get_object_or_404(DemonstracaoResultado, pk=pk)

    if request.method == "POST":
        form = DemostracaoResultadoForm(request.POST, instance=resultado)
        if form.is_valid():
            form.save()
            return redirect('demonstracao_resultados') # Redireciona para a tabela após edição
    else:
        form = DemostracaoResultadoForm(instance=resultado)

    return render(request, 'finance/edit_demonstracao_resultado.html', {'form': form})

def delete_demonstracao_resultado(request, pk):
    resultado = get_object_or_404(DemonstracaoResultado, pk=pk)
    resultado.delete()
    return redirect('demonstracao_resultados')

def demonstracao_resultados(request):
    resultados = DemonstracaoResultado.objects.all()

    # Cálculo dos valores
    receita_bruta = resultados.filter(descricao='Receita Bruta').first().valor if resultados.filter(descricao='Receita Bruta').exists() else 0
    deducoes_impostos = resultados.filter(descricao='(-) Deduções e Impostos').first().valor if resultados.filter(descricao='(-) Deduções e Impostos').exists() else 0
    receita_liquida = receita_bruta - deducoes_impostos
    custo_materiais_vendidos = resultados.filter(descricao='(-) Custo das Mercadorias Vendidas').first().valor if resultados.filter(descricao='(-) Custo das Mercadorias Vendidas').exists() else 0
    lucro_bruto = receita_liquida - custo_materiais_vendidos

    despesas_operacionais = resultados.filter(descricao='(-) Despesas Operacionais').first().valor if resultados.filter(descricao='(-) Despesas Operacionais').exists() else 0
    lucro_operacional = lucro_bruto - despesas_operacionais

    outras_receitas = resultados.filter(descricao='(+) Outras Receitas').first().valor if resultados.filter(descricao='(+) Outras Receitas').exists() else 0
    outras_despesas = resultados.filter(descricao='(-) Outras Despesas').first().valor if resultados.filter(descricao='(-) Outras Despesas').exists() else 0
    lucro_antes_impostos = lucro_operacional + outras_receitas - outras_despesas

    imposto_renda = resultados.filter(descricao='(-) Imposto de Renda').first().valor if resultados.filter(descricao='(-) Imposto de Renda').exists() else 0
    lucro_liquido = lucro_antes_impostos - imposto_renda

    context = {
        'resultados': resultados,
        'receita_liquida': receita_liquida,
        'custo_materiais_vendidos': custo_materiais_vendidos,
        'lucro_bruto': lucro_bruto,
        'despesas_operacionais': despesas_operacionais,
        'lucro_operacional': lucro_operacional,
        'outras_receitas': outras_receitas,
        'outras_despesas': outras_despesas,
        'lucro_antes_impostos': lucro_antes_impostos,
        'imposto_renda': imposto_renda,
        'lucro_liquido': lucro_liquido,
    }

    return render(request, 'finance/demonstracao_resultados.html', context)