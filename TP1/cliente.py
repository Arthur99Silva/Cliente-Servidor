#!/usr/bin/env python3

import socket
import sys

ROT = 13
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DESCONECTADO!"
SERVER = "192.168.0.112"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
user_input = print("Digite o endereço IP do servidor ou pressione ENTER ")

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def message(msg):
    if user_input != '':
        HOST = user_input
    user_input = print("Digite a porta de conexão com o servidor ou pressione ENTER para porta padrão ")
if user_input != '':
    PORT = int(user_input)
    servidor = (HOST, PORT)
    client.connect(servidor)
    print("Para sair use CTRL+X\n")
msg = print("Mensagem à enviar: ")
while msg != '\x18':    # Enquanto o usuário não usar a tecla "ESC"
    client.send(str.encode(msg))
    msg = print("Mensagem à enviar: ")
client.close()