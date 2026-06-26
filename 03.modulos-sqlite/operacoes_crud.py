# Módulo de operações CRUD - Conforme REQUERIMENTOS 4, 5, 6, 7, e 8.
import sqlite3
from modelos_enums import TipoAtivo, Severidade, StatusVulnerabilidade
from utilidades import ler_texto, ler_inteiro, escolher_enum
from banco_dados import inventario, sincronizar_memoria

# Função de cadastro de um ativo de TI 
def cadastrar_ativo():
    print("\n <<< 1. CADASTRAR ATIVO >>>\n")
    id_ativo = ler_inteiro(" > ID Único do Ativo")
    
    if id_ativo in inventario:
        print("Erro: ID já cadastrado no sistema.")
        return
        
    hostname = ler_texto(" > Hostname / Nome")
    responsavel = ler_texto(" > Responsável")
    setor = ler_texto(" > Setor / Localização")
    descricao = ler_texto(" > Descrição do Ativo")
    tipo_cod = escolher_enum(TipoAtivo, "Tipo de Ativo")
    
    with sqlite3.connect("inventario.db") as conn:
        conn.execute(
            "INSERT INTO ativos (id_ativo, hostname, responsavel, setor, descricao, tipo) VALUES (?, ?, ?, ?, ?, ?)",
            (id_ativo, hostname, responsavel, setor, descricao, tipo_cod)
        )
    print("\n > Ativo cadastrado!")
    
    if ler_texto("\nDeseja associar uma vulnerabilidade inicial? (S/N)", True).lower() == 's':
        desc_v = ler_texto("Descrição da Vulnerabilidade")
        cat_v = ler_texto("Categoria")
        sev_v = escolher_enum(Severidade, "Severidade")
        status_v = escolher_enum(StatusVulnerabilidade, "Status")
        
        with sqlite3.connect("inventario.db") as conn:
            conn.execute(
                "INSERT INTO vulnerabilidades (ativo_id, descricao, categoria, severidade, status) VALUES (?, ?, ?, ?, ?)",
                (id_ativo, desc_v, cat_v, sev_v, status_v)
            )
        print("Vulnerabilidade vinculada!")
        
    sincronizar_memoria()

# Função de atualização dos dados de um ativo conforme REQUERIMENTO 5
def atualizar_ativo():
    print("\n <<< 2. ATUALIZAR ATIVO >>>\n")
    id_ativo = ler_inteiro(" > ID do Ativo que deseja alterar")
    
    if id_ativo not in inventario:
        print(" >< Ativo não existe.")
        return
        
    dados = inventario[id_ativo]
    print("\n Aperte ENTER deixando vazio para NÃO alterar um campo. \n")
    
    novo_resp = ler_texto(f" > Responsável [{dados['responsavel']}]", True) or dados['responsavel']
    novo_setor = ler_texto(f" > Setor [{dados['setor']}]", True) or dados['setor']
    nova_desc = ler_texto(f" > Descrição [{dados['descricao']}]", True) or dados['descricao']
    
    mudar_tipo = ler_texto(" > Deseja mudar o Tipo de Ativo? (S/N)", True).lower()
    novo_tipo = escolher_enum(TipoAtivo, "Novo Tipo") if mudar_tipo == 's' else dados['tipo']
    
    with sqlite3.connect("inventario.db") as conn:
        conn.execute(
            "UPDATE ativos SET responsavel = ?, setor = ?, descricao = ?, tipo = ? WHERE id_ativo = ?",
            (novo_resp, novo_setor, nova_desc, novo_tipo, id_ativo)
        )
    print("\n > Ativo atualizado.")
    sincronizar_memoria()

# Função de deleção de um ativo e suas vulnerabilidades conforme REQUERIMENTO 6
def deletar_ativo():
    print("\n <<< 3. DELETAR ATIVO >>>\n")
    id_ativo = ler_inteiro(" ID do Ativo a ser deletado")
    
    if id_ativo in inventario:
        with sqlite3.connect("inventario.db") as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.execute("DELETE FROM ativos WHERE id_ativo = ?", (id_ativo,))
            
        print("\n > Registro do ativo e suas vulnerabilidades foram removidos.")
        sincronizar_memoria()
    else:
        print(" >< Ativo não encontrado.")

# Função de cadastro de vulnerabilidades de um ativo conforme REQUERIMENTO 7
def cadastrar_vulnerabilidade():
    print("\n <<< 4. CADASTRAR VULNERABILIDADE >>>\n")
    id_ativo = ler_inteiro("ID do Ativo afetado")
    
    if id_ativo not in inventario:
        print(" >< Ativo não encontrado.")
        return
        
    desc = ler_texto(" > Descrição do problema")
    cat = ler_texto(" > Categoria")
    sev = escolher_enum(Severidade, "Severidade")
    status = escolher_enum(StatusVulnerabilidade, "Status Atual")
    
    with sqlite3.connect("inventario.db") as conn:
        conn.execute(
            "INSERT INTO vulnerabilidades (ativo_id, descricao, categoria, severidade, status) VALUES (?, ?, ?, ?, ?)",
            (id_ativo, desc, cat, sev, status)
        )
    print("\n > Vulnerabilidade registrada.")
    sincronizar_memoria()

# Função de atualização de vulnerabilidade conforme enunciado - CRUD para vulns
def atualizar_vulnerabilidade():
    print("\n <<< 5. ATUALIZAR VULNERABILIDADE >>>\n")
    id_vuln = ler_inteiro(" > ID da Vulnerabilidade que deseja alterar")
   
    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
       
        # Corrigido
        cursor.execute("SELECT descricao, categoria, severidade, status FROM vulnerabilidades WHERE id_vuln = ?", (id_vuln,))
        vuln = cursor.fetchone()
       
        if not vuln:
            print("\n >< Erro: Vulnerabilidade não encontrada no banco de dados.")
            return
   
        # Corrigido
        desc_atual, cat_atual, sev_atual, status_atual = vuln

        print("\n > (Aperte ENTER deixando vazio para NÃO alterar um campo)")
       
        nova_desc = ler_texto(f" > Descrição [{desc_atual}]", permitir_vazio=True) or desc_atual
       
        nova_cat = ler_texto(f" > Categoria [{cat_atual}]", permitir_vazio=True) or cat_atual
       
        nova_sev = sev_atual
        if ler_texto(" > Deseja mudar a Severidade? (S/N)", permitir_vazio=True).lower() == 's':
            nova_sev = escolher_enum(Severidade, "Nova Severidade")
           
        novo_status = status_atual
        if ler_texto(" > Deseja mudar o Status? (S/N)", permitir_vazio=True).lower() == 's':
            novo_status = escolher_enum(StatusVulnerabilidade, "Novo Status")
           
        # Corrigido
        cursor.execute('''
            UPDATE vulnerabilidades
            SET descricao = ?, categoria = ?, severidade = ?, status = ?
            WHERE id_vuln = ?
        ''', (nova_desc, nova_cat, nova_sev, novo_status, id_vuln))
       
        # Corrigido
        conn.commit()
        
    print("\n > Vulnerabilidade atualizada!")


# Função de deleção de vulnerabilidade conforme enunciado - CRUD para vulns
def deletar_vulnerabilidade():
    print("\n <<< 6. REMOVER VULNERABILIDADE >>>\n")
    id_vuln = ler_inteiro(" > ID da Vulnerabilidade a ser removida")
   
    with sqlite3.connect("inventario.db") as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()
       
        # Corrigido
        cursor.execute("SELECT id_vuln FROM vulnerabilidades WHERE id_vuln = ?", (id_vuln,))
        if not cursor.fetchone():
            print("\n >< Erro: Vulnerabilidade não encontrada no banco de dados.")
            return
       
        # Corrigido
        cursor.execute("DELETE FROM vulnerabilidades WHERE id_vuln = ?", (id_vuln,))
        conn.commit()
   
    sincronizar_memoria()
    print("\n > Vulnerabilidade removida com sucesso!")

# Função de busca e exibição de ativos e suas vulns conforme REQUERIMENTOS 4 e 8
def consultar_ativo():
    print("\n <<< 7. CONSULTAR ATIVO e VULNS>>>\n")
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
            print("Este ativo está sem vulnerabilidades registradas.")
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
        print(" > Ativo não encontrado.")
