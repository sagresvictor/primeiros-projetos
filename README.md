# 🍽️ Sistema de Gestão de Reservas - Ristorante

Este é um sistema de backend desenvolvido em **Python** com persistência em **SQLite**, criado para gerenciar o fluxo de reservas de um restaurante de forma automatizada e segura.

## 🚀 Funcionalidades
- **Menu Interativo:** Interface via terminal amigável para o utilizador.
- **Operações CRUD:** Criar, Listar e Cancelar reservas diretamente no banco de dados.
- **Validação de Dados:** Filtros robustos que impedem a entrada de datas inexistentes ou horários inválidos (ex: 25:60).
- **Regras de Negócio:** Sistema de verificação de disponibilidade que impede reservas duplicadas para a mesma mesa, data e hora.
- **Automação de Saída:** Geração automática de um comprovante em formato `.txt` após a confirmação da reserva.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.14.3
- **Banco de Dados:** SQLite3 (Relacional)
- **Bibliotecas Nativas:** `os` (manipulação de caminhos), `datetime` (tratamento de tempo), `sqlite3` (conexão DB).

## 📂 Estrutura do Projeto
- `main.py`: Inicialização do banco de dados e criação das tabelas.
- `reservar.py`: Motor principal com as funções de lógica e o menu interativo.
- `restaurante.db`: Arquivo de base de dados relacional.

## ⚙️ Como Executar
1. Clone este repositório.
2. Certifique-se de ter o Python instalado.
3. Execute o `main.py` para preparar o ambiente.
4. Execute o `reservar.py` para iniciar o sistema.

---
Desenvolvido por **Victor Hugo Sagres** como projeto prático no curso de ADS.