# Módulo do banco de dados em SQLite - Conforme REQUERIMENTOS 9 e 11.
import sqlite3

# Uso de uma estrutura de dicionario para otimização conforme REQUERIMENTO 9. 
inventario = {}

# Criação e manutenção de um banco de dados relacional conforme REQUERIMENTO 11

# Função de inicialização do banco de dados relacional SQLite
def inicializar_banco():
    with sqlite3.connect("inventario.db") as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS ativos (
                id_ativo INTEGER PRIMARY KEY,
                hostname TEXT NOT NULL,
                responsavel TEXT NOT NULL,
                setor TEXT NOT NULL,
                descricao TEXT NOT NULL,
                tipo INTEGER NOT NULL
            )
        ''')
        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS vulnerabilidades (
                id_vuln INTEGER PRIMARY KEY AUTOINCREMENT,
                ativo_id INTEGER,
                descricao TEXT,
                categoria TEXT,
                severidade TEXT,
                status TEXT,
                FOREIGN KEY (ativo_id) REFERENCES ativos (id_ativo) ON DELETE CASCADE
            )
        ''')

# Função de carregamento dos dados do banco de dados relacional para o dicionário em memória 
def sincronizar_memoria():
    inventario.clear()
    with sqlite3.connect("inventario.db") as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT id_ativo, hostname, responsavel, setor, descricao, tipo FROM ativos")
        for linha in cursor.fetchall():
            id_ativo, hostname, responsavel, setor, descricao, tipo = linha
            inventario[id_ativo] = {
                "hostname": hostname, "responsavel": responsavel,
                "setor": setor, "descricao": descricao, "tipo": tipo, 
                "vulnerabilidades": []
            }
            
        cursor.execute("SELECT id_vuln, ativo_id, descricao, categoria, severidade, status FROM vulnerabilidades")
        for linha in cursor.fetchall():
            id_vuln, ativo_id, desc, cat, sev, status = linha
            if ativo_id in inventario:
                inventario[ativo_id]["vulnerabilidades"].append({
                    "id_vuln": id_vuln, "descricao": desc,
                    "categoria": cat, "severidade": sev, "status": status
                })
