import sqlite3

def conectar():
    return sqlite3.connect("imobiliaria.db")

def criar_tabelas():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS visitas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT,
        telefone TEXT,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()