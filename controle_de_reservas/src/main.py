import os

# Pega o caminho da pasta onde o SCRIPT está salvo
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))

# Define que o banco deve ficar obrigatoriamente NESSA pasta
caminho_banco = os.path.join(diretorio_do_script, 'restaurante.db')

import sqlite3  # Importa a biblioteca para lidar com banco de dados

# 1. Conectar ao banco de dados (se não existir, ele cria o arquivo 'restaurante.db')
conexao = sqlite3.connect('restaurante.db')

# 2. Criar um "cursor" (é o que usamos para executar comandos SQL no banco)
cursor = conexao.cursor()

# 3. Criar a tabela de MESAS
cursor.execute('''
CREATE TABLE IF NOT EXISTS mesas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_mesa INTEGER NOT NULL,
    capacidade INTEGER NOT NULL
)
''')

# 4. Criar a tabela de RESERVAS
# Note o 'id_mesa', que faz a ligação com a tabela de cima
cursor.execute('''
CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    data_reserva TEXT NOT NULL,
    horario TEXT NOT NULL,
    id_mesa INTEGER,
    FOREIGN KEY (id_mesa) REFERENCES mesas (id)
)
''')

# Salva as alterações e fecha a conexão inicial
conexao.commit()
conexao.close()

print("Banco de dados e tabelas criados com sucesso!")
