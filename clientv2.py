import socket
import threading
import os
import PySimpleGUI as sg


def connect():
    layout = [
        [sg.Text('Choose your nickname:'), sg.InputText(key='--NAME--')],
        [sg.Text('Server IP:'), sg.InputText(key='--IP--')],
        [sg.Text('Server Port:'), sg.InputText(key='--PORT--')],
        [sg.Button('Connect')]
    ]

    window = sg.Window('Chat Client', layout)

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == None:
        window.close()
        return
    
    nickname = values['--NAME--']
    # Connecting To Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((values['--IP--'], int(values['--PORT--'])))
    client.send(nickname.encode('utf-8'))
    window.close()

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

def chat_window():
    layout = [
        [sg.Multiline(size=(80, 20), key='--MSG--')],
        [sg.InputText(key='--MSGIN--'), [sg.FileBrowse(key='--FILE--')], [sg.Button('Send')]]
    ]
    window = sg.Window('Chat Client', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Send':
            message = values['--MSGIN--']
            if message == 'EXIT':  # Add an exit condition
                client.send(message.encode('utf-8'))
                break
            elif message.startswith('FILE'):  # Check if the message is a file
                file_path = message.split()[1]
                try:
                    with open(file_path, 'rb') as file:
                        file_data = file.read()
                    client.send(message.encode('utf-8'))
                    client.send(file_data)
                except:
                    print('File not found')
            else:
                client.send(message.encode('utf-8'))
            message = client.recv(1024).decode('utf-8')
            print(message)
            window['--MSG--'].print(message)
    client.close()