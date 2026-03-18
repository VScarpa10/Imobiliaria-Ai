from database import conectar

def horario_disponivel(data):

    conn = conectar()
    c = conn.cursor()

    c.execute("SELECT * FROM visitas WHERE data=?", (data,))
    visita = c.fetchone()

    conn.close()

    return visita is None


def marcar_visita(cliente, telefone, data):

    conn = conectar()
    c = conn.cursor()

    c.execute(
        "INSERT INTO visitas (cliente, telefone, data) VALUES (?, ?, ?)",
        (cliente, telefone, data)
    )

    conn.commit()
    conn.close()