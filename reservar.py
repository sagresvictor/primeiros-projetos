import os

# Pega o caminho da pasta onde o SCRIPT está salvo
diretorio_do_script = os.path.dirname(os.path.abspath(__file__))

# Define que o banco deve ficar obrigatoriamente NESSA pasta
caminho_banco = os.path.join(diretorio_do_script, 'restaurante.db')

import sqlite3
import os
from datetime import datetime

# --- CONFIGURAÇÕES DE CAMINHO (ESSENCIAL PARA ADS) ---
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_script, 'restaurante.db')

# --- FUNÇÕES DE APOIO (VALIDAÇÕES E TICKET) ---

def validar_data(data_texto):
    try:
        datetime.strptime(data_texto, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validar_horario(horario_texto):
    try:
        datetime.strptime(horario_texto, '%H:%M')
        return True
    except ValueError:
        return False

def gerar_ticket(nome, data, hora, mesa):
    nome_arquivo = f"ticket_{nome}_{data}.txt"
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("==========================================\n")
            arquivo.write("       COMPROVANTE DE RESERVA - RISTORANTE\n")
            arquivo.write("==========================================\n")
            arquivo.write(f" CLIENTE: {nome}\n")
            arquivo.write(f" DATA:    {data}\n")
            arquivo.write(f" HORÁRIO: {hora}\n")
            arquivo.write(f" MESA:    {mesa}\n")
            arquivo.write("------------------------------------------\n")
            arquivo.write(" Por favor, chegue com 10 min de antecedencia.\n")
            arquivo.write("==========================================\n")
        print(f"🎫 Ticket gerado com sucesso: {nome_arquivo}")
    except Exception as e:
        print(f"⚠️ Erro ao gerar ticket: {e}")

# --- FUNÇÕES PRINCIPAIS DO SISTEMA ---

def fazer_reserva(nome_cliente, data_reserva, horario, id_mesa):
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    
    # Verifica se a mesa já está ocupada
    cursor.execute("SELECT * FROM reservas WHERE id_mesa = ? AND data_reserva = ? AND horario = ?", 
                   (id_mesa, data_reserva, horario))
    
    if cursor.fetchone():
        print(f"\n❌ Erro: Mesa {id_mesa} ocupada em {data_reserva} às {horario}!")
    else:
        cursor.execute("INSERT INTO reservas (nome_cliente, data_reserva, horario, id_mesa) VALUES (?, ?, ?, ?)", 
                       (nome_cliente, data_reserva, horario, id_mesa))
        conexao.commit()
        print(f"\n✅ Reserva de {nome_cliente} confirmada no banco!")
        # Agora o Python já conhece a função gerar_ticket porque ela está lá no topo
        gerar_ticket(nome_cliente, data_reserva, horario, id_mesa)
    
    conexao.close()

def listar_reservas():
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM reservas")
    reservas = cursor.fetchall()
    
    print("\n--- RELATÓRIO DE RESERVAS ---")
    if not reservas:
        print("Nenhuma reserva encontrada.")
    for r in reservas:
        print(f"ID: {r[0]} | Cliente: {r[1]} | Data: {r[2]} | Hora: {r[3]} | Mesa: {r[4]}")
    print("----------------------------")
    conexao.close()

def cancelar_reserva(id_reserva):
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM reservas WHERE id = ?", (id_reserva,))
    reserva = cursor.fetchone()

    if reserva:
        cursor.execute("DELETE FROM reservas WHERE id = ?", (id_reserva,))
        conexao.commit()
        print(f"\n🗑️ Reserva ID {id_reserva} (Cliente: {reserva[1]}) foi cancelada.")
    else:
        print(f"\n⚠️ Erro: Nenhuma reserva encontrada com o ID {id_reserva}.")
    
    conexao.close()

# --- MENU INTERATIVO ---

if __name__ == "__main__":
    while True:
        print("\n=== SISTEMA DE RESERVAS JUNIOR ===")
        print("1. Fazer Reserva")
        print("2. Listar Reservas")
        print("3. Cancelar Reserva")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do Cliente: ")
            
            while True:
                data = input("Data (AAAA-MM-DD): ")
                if validar_data(data): break
                print("❌ Data inválida! Use o formato AAAA-MM-DD.")

            while True:
                hora = input("Horário (HH:MM): ")
                if validar_horario(hora): break
                print("❌ Horário inválido! Use o formato HH:MM (24h).")
            
            try:
                mesa = int(input("Número da Mesa: "))
                fazer_reserva(nome, data, hora, mesa)
            except ValueError:
                print("❌ Erro: O número da mesa deve ser um algarismo.")
            
        elif opcao == "2":
            listar_reservas()
            
        elif opcao == "3":
            try:
                id_cancela = int(input("Digite o ID da reserva para cancelar: "))
                cancelar_reserva(id_cancela)
            except ValueError:
                print("❌ Erro: Digite um número de ID válido.")
            
        elif opcao == "0":
            print("Encerrando... Bom descanso, Victor!")
            break
        else:
            print("Opção inválida!")