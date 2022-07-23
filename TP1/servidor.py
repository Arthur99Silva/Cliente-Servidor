import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = '192.168.2.113' #'192.168.0.112'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DESCONECTADO"
list_of_clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"NOVA CONEXAO {addr} CONECTADA.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("MENSAGEM RECEBIDA".encode(FORMAT))

    conn.close()
        
def start():
    server.listen()
    print(f"SERVIDOR ESCUTANDO ==> {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"ATIVOS {threading.activeCount() - 1}")

print("INICIANDO SERVIDOR...")

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close() 
                remove(clients)
start()

