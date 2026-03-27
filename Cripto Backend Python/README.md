# 🚀 Crypto Monitor Multi-Moedas

Este projeto é um **Dashboard de Criptomoedas** em tempo real, desenvolvido para monitorar Bitcoin, Ethereum e Solana. Ele une coleta automatizada de dados (Backend) com uma interface moderna e responsiva (Frontend).

## 📸 Visual do Projeto
![Dashboard-cripto.png]

## 🛠️ Tecnologias e Arquitetura
* **Linguagem:** Python 3.14
* **Framework Web:** Flask (Servidor e Rotas)
* **Banco de Dados:** SQLite3 (Armazenamento persistente)
* **Consumo de API:** Requests (Integração com CoinGecko)
* **Frontend:** HTML5, CSS3 e Chart.js para gráficos.

---

## 🚀 Como Instalar e Rodar o Projeto

Siga estes passos para configurar o ambiente e executar o monitor no seu computador:

### 1. Preparação do Ambiente
Clone o repositório e entre na pasta do projeto:

git clone https://github.com/sagresvictor/Cripto-Backend-Python.git
cd "Cripto Backend Python"


Crie e ative o seu ambiente virtual (venv):

PowerShell
# No Windows:
python -m venv venv
.\venv\Scripts\activate
Instale todas as dependências necessárias:

PowerShell
pip install -r requirements.txt
2. Execução 
Para o sistema funcionar, você precisa de dois terminais abertos ao mesmo tempo (ambos com o venv ativado):

Terminal 1 (O Coletor): Este script busca os preços na API e salva no banco de dados.

PowerShell
python coletor_cripto.py
Terminal 2 (O Dashboard): Este comando inicia o servidor do site.

PowerShell
python app.py
3. Visualização
Abra o seu navegador e acesse:
👉 http://127.0.0.1:5000
