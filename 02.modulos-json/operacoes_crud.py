# Módulo de operações CRUD - Conforme REQUERIMENTOS 4, 5, 6, 7, e 8.
from modelos_enums import TipoAtivo, Severidade, StatusVulnerabilidade
from utilidades import ler_texto, ler_inteiro, escolher_enum
from banco_dados import inventario, sincronizar_memoria, salvar_banco

def gerar_id_vuln() -> int:
    max_id = 0
    for ativo in inventario.values():
        for vuln in ativo["vulnerabilidades"]:
            if vuln["id_vuln"] > max_id:
                max_id = vuln["id_vuln"]
    return max_id + 1

# Função de cadastro de um ativo de TI
def cadastrar_ativo():
    print("\n <<< 1. CADASTRAR ATIVO >>>\n")
    id_ativo = ler_inteiro(" > ID Único do Ativo")
    
    if id_ativo in inventario:
        print("\n >< Erro: ID já cadastrado no sistema.")
        return
        
    hostname = ler_texto(" > Hostname / Nome")
    responsavel = ler_texto(" > Responsável")
    setor = ler_texto(" > Setor / Localização")
    descricao = ler_texto(" > Descrição do Ativo")
    tipo_cod = escolher_enum(TipoAtivo, "Tipo de Ativo")
    
    inventario[id_ativo] = {
        "hostname": hostname, "responsavel": responsavel,
        "setor": setor, "descricao": descricao, "tipo": tipo_cod, 
        "vulnerabilidades": []
    }
    salvar_banco() 
    print("\n > Ativo cadastrado.")
    
    if ler_texto("\n > Deseja associar uma vulnerabilidade inicial? (S/N)", True).lower() == 's':
        desc_v = ler_texto("\n > Descrição da Vulnerabilidade")
        cat_v = ler_texto(" > Categoria")
        sev_v = escolher_enum(Severidade, "Severidade")
        status_v = escolher_enum(StatusVulnerabilidade, "Status")
        
        nova_vuln = {
            "id_vuln": gerar_id_vuln(),
            "descricao": desc_v,
            "categoria": cat_v,
            "severidade": sev_v,
            "status": status_v
        }
        inventario[id_ativo]["vulnerabilidades"].append(nova_vuln)
        salvar_banco()
        print("\n > Vulnerabilidade vinculada.")

# Função de atualização dos dados de um ativo conforme REQUERIMENTO 5
def atualizar_ativo():
    print("\n <<< 2. ATUALIZAR ATIVO >>>\n")
    id_ativo = ler_inteiro(" > ID do Ativo que deseja alterar")
    
    if id_ativo not in inventario:
        print("\nAtivo não existe.")
        return
        
    dados = inventario[id_ativo]
    print("\n > (Aperte ENTER deixando vazio para NÃO alterar um campo)")
    
    dados['responsavel'] = ler_texto(f" > Responsável [{dados['responsavel']}]", True) or dados['responsavel']
    dados['setor'] = ler_texto(f" > Setor [{dados['setor']}]", True) or dados['setor']
    dados['descricao'] = ler_texto(f" > Descrição [{dados['descricao']}]", True) or dados['descricao']
    
    mudar_tipo = ler_texto(" > Deseja mudar o Tipo de Ativo? (S/N)", True).lower()
    if mudar_tipo == 's':
        dados['tipo'] = escolher_enum(TipoAtivo, "Novo Tipo")
    
    salvar_banco()
    print("\n > Ativo atualizado!")

# Função de deleção de um ativo e suas vulnerabilidades conforme REQUERIMENTO 6
def deletar_ativo():
    print("\n <<< 3. DELETAR ATIVO >>>\n")
    id_ativo = ler_inteiro("ID do Ativo a ser deletado")
    
    if id_ativo in inventario:
        del inventario[id_ativo]
        salvar_banco()
        print(" > Registro do ativo e suas vulnerabilidades foram removidos!")
    else:
        print(" > Ativo não encontrado.")

# Função de cadastro de vulnerabilidades de um ativo conforme REQUERIMENTO 7
def cadastrar_vulnerabilidade():
    print("\n <<< 4. CADASTRAR VULNERABILIDADE >>>\n")
    id_ativo = ler_inteiro(" > ID do Ativo afetado")
    
    if id_ativo not in inventario:
        print("\n >< Ativo não encontrado.")
        return
        
    desc = ler_texto(" > Descrição do problema")
    cat = ler_texto(" > Categoria")
    sev = escolher_enum(Severidade, "Severidade")
    status = escolher_enum(StatusVulnerabilidade, "Status Atual")
    
    nova_vuln = {
        "id_vuln": gerar_id_vuln(),
        "descricao": desc,
        "categoria": cat,
        "severidade": sev,
        "status": status
    }
    
    inventario[id_ativo]["vulnerabilidades"].append(nova_vuln)
    salvar_banco()
    print("\n > Vulnerabilidade registrada.")

# Função de atualização de vulnerabilidade
def atualizar_vulnerabilidade():
    print("\n <<< 5. ATUALIZAR VULNERABILIDADE >>>\n")
    id_ativo = ler_inteiro(" > ID do Ativo afetado")
    
    if id_ativo not in inventario:
        print("\n >< Erro: Ativo não encontrado.")
        return
        
    falhas = inventario[id_ativo]["vulnerabilidades"]
    if not falhas:
        print("\n >< Erro: Este ativo não possui vulnerabilidades cadastradas.")
        return
        
    id_vuln = ler_inteiro(" > ID da Vulnerabilidade que deseja alterar")
    
    vuln_alvo = None
    for v in falhas:
        if v["id_vuln"] == id_vuln:
            vuln_alvo = v
            break
            
    if not vuln_alvo:
        print("\n >< Erro: Vulnerabilidade não encontrada neste ativo.")
        return

    print("\n > (Aperte ENTER deixando vazio para NÃO alterar um campo)")
    
    vuln_alvo['descricao'] = ler_texto(f" > Descrição [{vuln_alvo['descricao']}]", 
    permitir_vazio=True) or vuln_alvo['descricao']
                             # Corrigido
    
    vuln_alvo['categoria'] = ler_texto(f" > Categoria [{vuln_alvo['categoria']}]", 
    permitir_vazio=True) or vuln_alvo['categoria']
                             # Corrigido
    
    if ler_texto(" > Deseja mudar a Severidade? (S/N)", permitir_vazio=True).lower() == 's':
        vuln_alvo['severidade'] = escolher_enum(Severidade, "Nova Severidade")
       # Corrigido
    
    if ler_texto(" > Deseja mudar o Status? (S/N)", permitir_vazio=True).lower() == 's':
        vuln_alvo['status'] = escolher_enum(StatusVulnerabilidade, "Novo Status")
       # Corrigido
    salvar_banco()
    print("\n > Vulnerabilidade atualizada!")

# Função de deleção de vulnerabilidade
def deletar_vulnerabilidade():
    print("\n <<< 6. REMOVER VULNERABILIDADE >>>\n")
    id_ativo = ler_inteiro(" > ID do Ativo afetado")
    
    if id_ativo not in inventario:
        print("\n >< Erro: Ativo não encontrado.")
        return
        
    falhas = inventario[id_ativo]["vulnerabilidades"]
    if not falhas:
        print("\n >< Erro: Este ativo não possui vulnerabilidades cadastradas.")
        return
        
    id_vuln = ler_inteiro(" > ID da Vulnerabilidade a ser removida")
    
    tamanho_original = len(falhas)
    inventario[id_ativo]["vulnerabilidades"] = [v for v in falhas if v["id_vuln"] != id_vuln]
    
    if len(inventario[id_ativo]["vulnerabilidades"]) < tamanho_original:
        salvar_banco()
        print("\n > Vulnerabilidade removida com sucesso!")
    else:
        print("\n >< Erro: Vulnerabilidade não encontrada neste ativo.")

# Função de busca e exibição de ativos e suas vulns conforme REQUERIMENTOS 4 e 8
def consultar_ativo():
    print("\n <<< 7. CONSULTAR ATIVO >>>\n")
    termo = ler_texto("Digite o ID ou Hostname").lower()
    
    dados_encontrados = None
    id_encontrado = None
    
    if termo.isdigit() and int(termo) in inventario:
        id_encontrado = int(termo)
        dados_encontrados = inventario[id_encontrado]
    else:
        for id_ativo, info in inventario.items():
            if info["hostname"].lower() == termo:
                id_encontrado = id_ativo
                dados_encontrados = info
                break
                
    if dados_encontrados:
        print("\n" + "=" * 80)
        print(f" 1. DADOS DO ATIVO: {dados_encontrados['hostname']}")
        print("=" * 80)
        tipo_nome = TipoAtivo(dados_encontrados['tipo']).name
        
        print(f" > ID: {id_encontrado}")
        print(f" > Tipo: {tipo_nome} [Código {dados_encontrados['tipo']}]")
        print(f" > Responsável: {dados_encontrados['responsavel']}")
        print(f" > Setor: {dados_encontrados['setor']}")
        print(f" > Descrição: {dados_encontrados['descricao']}")
        print("-" * 80 + "\n")
        
        falhas = dados_encontrados["vulnerabilidades"]
        if not falhas:
            print("\nEste ativo está sem vulnerabilidades registradas.")
        else:
            print("=" * 80)
            print(" 2. VULNERABILIDADES:")
            for f in falhas:
                print("=" * 80)
                print(f" > ID: {f['id_vuln']}")
                print(f" > Descrição: {f['descricao']}")
                print(f" > Categoria: {f['categoria']}")
                print(f" > Severidade: {f['severidade']}")
                print(f" > Status: {f['status']}")
        print("=" * 80)
    else:
        print("\nAtivo não encontrado.")
