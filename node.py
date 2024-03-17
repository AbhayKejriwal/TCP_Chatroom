import os
import threading
import socket

node = {
  'ip': '',
  'port': 42424,
}
# Lists For Clients and Servers
server = []
clients = []
nicknames = []

def start_server():
  ''' function to start a server'''
  # Connection Data
  host = ''
  port = 42424
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((host, port))
  server.listen()


def connect_to_server(nodeIP, nodePort):
  ''' function to connect to a server port of an existing node to join the network'''
  # Connecting to a server
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((nodeIP, nodePort))


def send_message(message):
  ''' function to send message to all connected clients and server'''
  message = message.encode('utf-8')
  for client in clients:
    client.send(message)
  server.send(message)

def generate_message(inputText):
  message = {
    'type': '',
    'data': '',
  }
  if inputText == 'EXIT':  # Add an exit condition
    message['type'] = 'EXIT'
    message['data'] = ''
    break
  elif message.startswith('FILE'):  # Check if the message is a file
    file_path = inputText.split()[1]
    try:
      with open(file_path, 'rb') as file:
        file_data = file.read()
        file_name = os.path.basename(file_path)  # Extract the file name from the path
        message['type'] = 'FILE'
        message['data'] = file_data
    except FileNotFoundError:
      print('File not found.')
  else:
    message['type'] = 'TEXT'
    message['data'] = inputText
