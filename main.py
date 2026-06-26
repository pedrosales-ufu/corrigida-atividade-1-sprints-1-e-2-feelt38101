# Arquivo principal - Conforme REQUERIMENTO 1.
import os
from banco_dados import inicializar_banco, sincronizar_memoria
from operacoes_crud import (
    cadastrar_ativo, consultar_ativo, atualizar_ativo, 
    deletar_ativo, cadastrar_vulnerabilidade,
    atualizar_vulnerabilidade, deletar_vulnerabilidade     # Corrigido
)

def iniciar_sistema():
    inicializar_banco()
    sincronizar_memoria()

# Menu textual para interagir com o usuário conforme REQUERIMENTO 1    
    while True:
        print("\n" + "=" * 80)
        print(" <<< INVENTÁRIO DE ATIVOS DE TI >>>")
        print("=" * 80 + "\n")
        print(" [1] Cadastrar Ativo")
        print(" [2] Atualizar Ativo")
        print(" [3] Remover Ativo")
        print(" [4] Cadastrar Vulnerabilidade")
        print(" [5] Atualizar Vulnerabilidade")
        print(" [6] Remover Vulnerabilidade")
        print(" [7] Consultar Ativo e Vulnerabilidades Associadas")
        print(" [0] Sair")
        print("\n" + "=" * 80)
        
        opcao = input("\n > Escolha uma opção: ").strip()
        
        match opcao:
            case "1": cadastrar_ativo()                  # Create
            case "2": atualizar_ativo()                  # Update
            case "3": deletar_ativo()                    # Delete
            case "4": cadastrar_vulnerabilidade()        # Create
            case "5": atualizar_vulnerabilidade()        # Update 
            case "6": deletar_vulnerabilidade()          # Delete
            case "7": consultar_ativo()                  # Read
            case "0":
                print("\n > Encerrando...")
                break
            case _:
                print("\n > Comando inválido. Escolha de 0 a 7.") # Corrigido

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    iniciar_sistema()
