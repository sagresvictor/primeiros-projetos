import requests
import sqlite3
import time
from datetime import datetime

def buscar_preco(id_moeda):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={id_moeda}&vs_currencies=usd"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        return dados[id_moeda]['usd']
    except:
        return None

# 1. Definimos a lista com as 3 moedas solicitadas
moedas_alvo = ["bitcoin", "ethereum", "solana"]

while True:
    conexao = sqlite3.connect("cripto_dados.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS precos 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, moeda TEXT, preco REAL, data_hora TEXT)''')

    # 2. Criamos um laço 'for' para percorrer a lista
    for m in moedas_alvo:
        valor = buscar_preco(m)
        if valor:
            agora = datetime.now().strftime("%H:%M:%S")
            # 3. Salvamos cada moeda individualmente no banco
            cursor.execute("INSERT INTO precos (moeda, preco, data_hora) VALUES (?, ?, ?)", (m, valor, agora))
            print(f"Sucesso: {m} atualizado.")

    conexao.commit()
    conexao.close()
    time.sleep(30) # Espera 30 segundos e repete tudo novamente