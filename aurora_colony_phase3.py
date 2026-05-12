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