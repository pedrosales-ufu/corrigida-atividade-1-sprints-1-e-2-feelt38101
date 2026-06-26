# Módulo de enumerações - Conforme REQUERIMENTO 2.
from enum import Enum

# Lista de tipos de ativos de TI em Enum, conforme REQUERIMENTO 2
class TipoAtivo(Enum):
    SMARTPHONE = 1
    NOTEBOOK = 2
    SERVIDOR = 3
    ROTEADOR = 4
    FIREWALL = 5
    WEB_APP = 6

# Enum para registro de grau de severidade de uma vulnerabilidade
class Severidade(Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"
    CRITICA = "Crítica"

# Enum para registro de status de tratamento de uma vulnerabilidade
class StatusVulnerabilidade(Enum):
    ABERTA = "Aberta"
    EM_TRATAMENTO = "Em Tratamento"
    CORRIGIDA = "Corrigida"
    ACEITA = "Risco Aceito"
