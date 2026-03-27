from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conexao = sqlite3.connect("cripto_dados.db")
    cursor = conexao.cursor()
    
    # 1. Busca o último preço de cada uma das 3 moedas para a tabela
    cursor.execute("""
        SELECT moeda, preco, data_hora FROM precos 
        WHERE id IN (SELECT MAX(id) FROM precos GROUP BY moeda)
    """)
    dados_das_moedas = cursor.fetchall()
    
    # 2. Busca o histórico do Bitcoin para o gráfico (últimas 15 coletas)
    # Importante: o HTML espera 'precos_grafico' e 'horas_grafico'
    cursor.execute("SELECT preco, data_hora FROM precos WHERE moeda='bitcoin' ORDER BY id DESC LIMIT 15")
    historico = cursor.fetchall()[::-1] # Inverte para o gráfico fluir da esquerda para a direita
    
    eixo_precos = [h[0] for h in historico]
    eixo_horas = [h[1] for h in historico]

    conexao.close()

    # 3. ENVIO DAS VARIÁVEIS (Aqui é onde resolvemos o erro!)
    return render_template("index.html", 
                           lista_precos=dados_das_moedas, 
                           precos_grafico=eixo_precos, 
                           horas_grafico=eixo_horas)

if __name__ == "__main__":
    app.run(debug=True)