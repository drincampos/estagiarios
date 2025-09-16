from django.shortcuts import render, get_object_or_404
from estagiarios.models import Estagiario, UnidadesCLDF, MESA_DIRETORA, NIVEL_ACADEMICO
from datetime import datetime, timedelta

def proximo_saida(estagiario):

    dt_inicio_estagio = estagiario.data_inicio
    meses_duracao = estagiario.duracao_estagio
    dt_final_estagio = dt_inicio_estagio + timedelta(days=((meses_duracao-1) * 30))
    data_atual = datetime.now().date()
    sai_proximo_mes = True if data_atual > dt_final_estagio else False
    
    return {
        'id': estagiario.id,
        'dt_ini': dt_inicio_estagio, 
        'dt_fim': dt_final_estagio,
        'sai_proximo_mes': sai_proximo_mes
    }

def lista_proximos_sair(estagiarios):

    proximos_sair = []
    for estagiario in estagiarios:
        status = proximo_saida(estagiario)
        if status['sai_proximo_mes']:
            proximos_sair.append({
                'estagiario': estagiario,
                'dt_final': status['dt_fim']
            })
    
    return proximos_sair


def index(request):

    quantitativos_unidades = []
    for sigla in MESA_DIRETORA:

        unidades = UnidadesCLDF.objects.filter(subordinacao=sigla)
        total_estagiarios_und_mesa = 0
        total_nivel_medio = 0
        total_nivel_superior = 0
        total_proximos_saida = 0

        estagiarios_unidade = []
        for unidade in unidades:

            lista_estagiarios_unidade = Estagiario.objects.filter(unidade_cldf=unidade)
            qtde_estagiarios_unidade = lista_estagiarios_unidade.count()
            total_estagiarios_und_mesa += qtde_estagiarios_unidade            

            total_nivel_medio += lista_estagiarios_unidade.filter(nivel="2G").count()
            total_nivel_superior += lista_estagiarios_unidade.filter(nivel="SP").count()
            total_proximos_saida += lista_proximos_sair(lista_estagiarios_unidade).__len__()

            estagiarios_unidade.append({'unidade': unidade.nome_unidade, 'qtde': qtde_estagiarios_unidade})

        quantitativos_unidades.append({
            'sigla_und_mesa': sigla,
            'nome_und_mesa': MESA_DIRETORA[sigla],
            'total': total_estagiarios_und_mesa,
            'total_nivel_medio': total_nivel_medio,
            'total_nivel_superior': total_nivel_superior,
            'total_proximos_sair': total_proximos_saida,
            'estagiarios_unidade': estagiarios_unidade
        })
      

    return render(request, 'index.html', {'quantitativos_unidades': quantitativos_unidades})


