import socket
import os
import threading

# Connection Data
host = '192.168.29.112'
port = 42424

# Choosing Nickname
nickname = input("Choose your nickname: ")

# File Folder Path
file_folder = 'files_received'

# Create File Folder if it doesn't exist
if not os.path.exists(file_folder):
    os.makedirs(file_folder)

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            elif message.startswith('FILE '):  # Check if the message is a file
                file_name = message.split()[1]
                file_data = client.recv(4096)
                save_file(file_name, file_data)
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break

# Saving File Data to a File
def save_file(file_name, file_data):
    file_path = os.path.join(file_folder, file_name)
    with open(file_path, 'wb') as file:
        file.write(file_data)
    print(f'Saved file: {file_name}')

# Sending Messages To Server
def write():
    while True:
        message = input('')
        if message == 'EXIT':  # Add an exit condition
            client.send(message.encode('utf-8'))
            break
        elif message.startswith('FILE'):  # Check if the message is a file
            file_path = message.split()[1]
            try:
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                file_name = os.path.basename(file_path)  # Extract the file name from the path
                message = f'FILE {file_name}'
                client.sendall(message.encode('utf-8'))
                client.sendall(file_data)
            except FileNotFoundError:
                print('File not found.')
        else:
            client.send(message.encode('utf-8'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
