# Aurora Siger — Sistema Integrado de Gestão da Colônia (Fase 3)

**FIAP | Ciência da Computação | Grupo:** Gabriel, Lucas, Matheus, Miguel e Pedro

---

## Descrição

Sistema computacional autônomo desenvolvido para gerenciar a operação contínua da colônia Aurora Siger em Marte. A cada execução, sensores simulados geram leituras aleatórias dentro de faixas operacionais reais, e o sistema analisa, prevê e decide sem intervenção humana.

---

## Funcionalidades

| Bloco | Função |
|---|---|
| Estrutura de dados | Organização hierárquica da colônia em dicionários e listas |
| Análise de energia | Comparação entre geração, consumo e carga das baterias |
| Previsões | Regressão linear simples para estimar energia eólica e consumo futuro |
| Motor de decisão | Regras automáticas com priorização de sistemas essenciais |

---

## Como executar

Requer apenas **Python 3** — sem dependências externas.

```bash
python aurora_colony.py
```

Cada execução gera um cenário diferente com base em valores aleatórios dos sensores.

---

## Exemplo de cenário (valores variam a cada execução)

**Cenário: consumo maior que geração**

Entrada (gerada automaticamente pelos sensores):
```
Solar    : 35.1 kW
Eolico   : 5.2 kW
Baterias : 53.8%
Consumo  : 45.3 kW
```

Saída do sistema:
```
  [ALERTA] Consumo maior que geracao. Usando reserva das baterias.

  Modelo eolico  : energia = 0.631 * vento + (-0.118)
  Energia prevista: 34.8 kW

  [ALERTA] Modo economia ativado.
  -> Reduzindo 30% do consumo dos modulos de baixa prioridade:
     REDUZIDO: Laboratorio Cientifico -> 8.9 kW
     REDUZIDO: Logistica e Suprimentos -> 4.8 kW
```

---

## Regras de decisão

| Condição | Ação |
|---|---|
| Baterias < 30% **e** consumo > geração | EMERGÊNCIA — desliga módulos com prioridade < 3 |
| Consumo > geração | ALERTA — reduz 30% do consumo dos módulos não essenciais |
| Baterias < 50% | AVISO — mantém operação, prioriza recarga |
| Excedente > 20 kW | OK — redireciona excedente para baterias |
| Tudo estável | OK — operação normal |

Módulos com **prioridade ≥ 3** (Suporte Médico, Geração de Energia, Habitação Principal) nunca são desligados.

---

## Estrutura do código

```
aurora_colony.py
├── Bloco 1 — Estrutura de dados da colônia
├── Bloco 2 — Funções auxiliares
├── Bloco 3 — Regressão linear simples
├── Bloco 4 — Análise de energia
├── Bloco 5 — Motor de decisão automatizado
├── Bloco 6 — Previsões
└── Bloco 7 — Painel de status e execução principal
```
