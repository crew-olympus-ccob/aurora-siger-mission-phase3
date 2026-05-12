# =============================================================================
#  AURORA SIGER — SISTEMA INTEGRADO DE GESTÃO DA COLÔNIA (Fase 3)
#  FIAP | Ciência da Computação | Grupo: Gabriel, Lucas, Matheus, Miguel e Pedro
# =============================================================================

# =============================================================================
#  BLOCO 1 — ESTRUTURA DE DADOS DA COLÔNIA (hierárquica + chave-valor + listas)
# =============================================================================

# Hierarquia principal: colônia → sistema → subsistema → atributos
import random

colonia = {
    "energetico": {
        "solar":    {"geracao_kw": random.uniform(0.0, 80.0),  "status": "OK"},
        "eolico":   {"geracao_kw": random.uniform(0.0, 30.0),  "status": "OK"},
        "baterias": {"carga_pct": random.uniform(10.0, 100.0), "status": "OK"}
    },
    "ambiental": {
        "temperatura_interna_c": random.uniform(5.0, 40.0),
        "temperatura_externa_c": random.uniform(-60.0, 20.0),
        "vento_kmh": random.uniform(0.0, 80.0)
    },
    "operacional": {
        "modulos": [
            {"nome": "Suporte Medico",         "consumo_kw": random.uniform(5.0, 12.0),  "prioridade": 5, "status": "OK"},
            {"nome": "Geracao de Energia",      "consumo_kw": random.uniform(1.0, 5.0),   "prioridade": 4, "status": "OK"},
            {"nome": "Habitacao Principal",     "consumo_kw": random.uniform(10.0, 20.0), "prioridade": 3, "status": "OK"},
            {"nome": "Laboratorio Cientifico",  "consumo_kw": random.uniform(6.0, 14.0),  "prioridade": 2, "status": "OK"},
            {"nome": "Logistica e Suprimentos", "consumo_kw": random.uniform(3.0, 9.0),   "prioridade": 1, "status": "OK"}
        ]
    }
}


# =============================================================================
#  BLOCO 2 — FUNÇÕES AUXILIARES
# =============================================================================

def calcular_geracao_total():
    e = colonia["energetico"]
    return e["solar"]["geracao_kw"] + e["eolico"]["geracao_kw"]


def calcular_consumo_total():
    total = 0.0
    for mod in colonia["operacional"]["modulos"]:
        if mod["status"] != "DESLIGADO":
            total += mod["consumo_kw"]
    return total


def obter_estado_energia():
    geracao = calcular_geracao_total()
    consumo = calcular_consumo_total()
    carga   = colonia["energetico"]["baterias"]["carga_pct"]
    return geracao, consumo, carga


# =============================================================================
#  BLOCO 3 — REGRESSÃO LINEAR SIMPLES (sem bibliotecas externas)
#
#  Fórmula:
#       a = (n·Σxy − Σx·Σy) / (n·Σx² − (Σx)²)
#       b = (Σy − a·Σx) / n
#       y_estimado = a*x + b
# =============================================================================

# Histórico de sensores: vento (km/h) × energia eólica gerada (kW)
historico_vento_kmh      = [round(random.uniform(5.0, 25.0), 1) for _ in range(7)]
historico_energia_eolica = [round(v * 0.65 + random.uniform(-1.0, 1.0), 1) for v in historico_vento_kmh]

# Histórico de consumo ao longo do dia (hora × kW total consumido)
historico_hora_do_dia = [6, 8, 10, 12, 14, 16, 18]
historico_consumo_kw  = [round(random.uniform(25.0, 35.0) + h * 0.8, 1) for h in historico_hora_do_dia]


def regressao_linear(xs, ys):
    n       = len(xs)
    soma_x  = sum(xs)
    soma_y  = sum(ys)
    soma_xy = sum(xs[i] * ys[i] for i in range(n))
    soma_x2 = sum(x ** 2 for x in xs)

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    b = (soma_y - a * soma_x) / n
    return a, b


def prever_energia_eolica(vento_kmh):
    a, b = regressao_linear(historico_vento_kmh, historico_energia_eolica)
    return max(0.0, round(a * vento_kmh + b, 2))


def prever_consumo_por_hora(hora):
    a, b = regressao_linear(historico_hora_do_dia, historico_consumo_kw)
    return max(0.0, round(a * hora + b, 2))