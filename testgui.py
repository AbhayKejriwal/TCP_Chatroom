import PySimpleGUI as sg

layout = [
        [sg.Output(size=(71, 20), key='--CHATS--')],
        [sg.Multiline(size=(50, 5), key='--MSGS--', do_not_clear=False, enter_submits=True), 
         sg.Button('Send', size=(7, 3)), sg.FileBrowse(key='--FILE--', size=(7, 3)) 
        ]
]

window = sg.Window('Chat Client', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        break
    if event == 'Send' or event == '--MSGS--':
        message = values['--MSGS--']
        #print to message box
        window['--CHATS--'].print(message)
    elif event == '--FILE--':
        file_path = values['--FILE--']
        #print to message box
        window['--CHATS--'].print(file_path)
        #try:
        #    with open(file_path, 'rb') as file:
        #        file_data = file.read()
        #    client.send(message.encode('utf-8'))
        #    client.send(file_data)
        #except:
        #    print('File not found')
    
    