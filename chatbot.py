from openai import OpenAI
from agenda import marcar_visita, horario_disponivel

client = OpenAI()

def responder(mensagem, cliente, telefone):

    mensagem_lower = mensagem.lower()

    if "visita" in mensagem_lower:

        return "Claro! Qual dia e horário você gostaria de visitar o imóvel? (ex: 25/03/2026 15:00)"

    if "/" in mensagem and ":" in mensagem:

        if horario_disponivel(mensagem):

            marcar_visita(cliente, telefone, mensagem)

            return f"Perfeito! Visita agendada para {mensagem}. O corretor irá te encontrar no imóvel."

        else:

            return "Esse horário já está ocupado. Poderia escolher outro?"

    # resposta usando IA
    prompt = f"""
    Você é um assistente de vendas de uma imobiliária.
    Responda de forma educada e profissional.

    Cliente: {mensagem}
    """

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Assistente de vendas imobiliárias."},
            {"role": "user", "content": prompt}
        ]
    )

    return resposta.choices[0].message.content