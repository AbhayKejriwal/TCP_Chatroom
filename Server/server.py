import socket
import threading

# Connection Data
host = ''
port = 42424

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Receive Message From Client
            message = client.recv(4096)
            if message.startswith(b'FILE '):  # Check if the message is a file
                file_name = message.decode('utf-8').split()[1]
                file_data = client.recv(4096)
                save_file(file_name, file_data)
            else:
                broadcast(f'{nicknames[clients.index(client)]}: {message.decode("utf-8")}'.encode('utf-8'))
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            print(f'{nickname} left!')
            broadcast(f'{nickname} left!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Save File Function; also broadcasts only the file name
def save_file(file_name, file_data):
    try:
        with open(file_name, 'wb') as file:
            file.write(file_data)
        print(f'Saved file: {file_name}')
        broadcast(f'Saved file: {file_name}'.encode('utf-8'))
    except:
        print(f'Failed to save file: {file_name}')
        broadcast(f'Failed to save file: {file_name}'.encode('utf-8'))

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Request And Store Nickname
        client.send(b'NICK')
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined!".encode('utf-8'))
        client.send(b'Connected to server!')

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
