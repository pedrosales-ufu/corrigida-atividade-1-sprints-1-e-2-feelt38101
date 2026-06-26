# Módulo do banco de dados em json - Conforme REQUERIMENTOS 3 e 9.
import json
import os

# Uso de uma estrutura de dicionario para otimização conforme REQUERIMENTO 9. 
inventario = {}
ARQUIVO_DB = "inventario.json"

# Criação e manutenção do banco de dados em json conforme REQUERIMENTO 3

# Função de inicialização do banco de dados em formato json
def inicializar_banco():
    if not os.path.exists(ARQUIVO_DB):
        with open(ARQUIVO_DB, 'w', encoding='utf-8') as f:
            json.dump({}, f)

# Função de carregamento dos dados do json para o dicionário em memória 
def sincronizar_memoria():
    inventario.clear()
    try:
        with open(ARQUIVO_DB, 'r', encoding='utf-8') as f:
            dados_brutos = json.load(f)
            for id_str, dados in dados_brutos.items():
                inventario[int(id_str)] = dados
    except (FileNotFoundError, json.JSONDecodeError):
        inventario.clear()

# Função de sobrescrita do arquivo json pelos dados atuais da memória
def salvar_banco():
    with open(ARQUIVO_DB, 'w', encoding='utf-8') as f:
        json.dump(inventario, f, ensure_ascii=False, indent=4)
