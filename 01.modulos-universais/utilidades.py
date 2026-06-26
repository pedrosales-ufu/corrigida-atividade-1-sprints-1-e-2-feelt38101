# Módulo de utilidades com funções auxiliares - Conforme REQUERIMENTO 1.
from modelos_enums import TipoAtivo

# Funções auxiliares para tratamento de erros conforme REQUERIMENTO 1

# Função para validação de dados de entrada em formato textual
def ler_texto(mensagem: str, permitir_vazio: bool = False) -> str:
    while True:
        valor = input(f"{mensagem}: ").strip()
        if not valor and not permitir_vazio:
            print("\n >< Erro: Este campo não pode ficar vazio.\n")
            continue
        return valor

# Função para validação de dados de entrada em formato numerico inteiro
def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(f"{mensagem}: ").strip())
        except ValueError:
            print("\n >< Erro: Entrada inválida. Digite apenas números inteiros.\n")

# Função auxiliar para validação de dados de entrada 
def escolher_enum(enum_class, titulo: str):
    print(f"\n<<< {titulo} >>>")
    opcoes = list(enum_class)
    for idx, opcao in enumerate(opcoes, 1):
        print(f" [{idx}] - {opcao.name if isinstance(opcao, TipoAtivo) else opcao.value}")
        
    while True:
        escolha = ler_inteiro("\n > Escolha uma opção numérica")
        if 1 <= escolha <= len(opcoes):
            return opcoes[escolha - 1].value
        print(f"\n >< Erro: Escolha entre 1 e {len(opcoes)}.")
