
# Chat Application with File Transfer

This project is a simple Python-based chat application with file transfer functionality. It allows multiple clients to connect to a central server and exchange text messages and files. The project is implemented using Python's socket library and multi-threading for concurrent client handling.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Server](#running-the-server)
  - [Running a Client](#running-a-client)
  - [Connecting from Different Devices](#connecting-from-different-devices)
- [Features](#features)
  - [Text Chat](#text-chat)
  - [File Transfer](#file-transfer)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

To run this project, you'll need:

- Python (3.x recommended)

### Running the Server

1. Clone the repository to your local machine.
2. Open a terminal in the project directory.
3. Run the server using the following command:

```
python server.py
```

The server will start listening on a specified port (default is 42424).

### Running a Client

1. Clone the repository to a different directory on your local machine.
2. Open a terminal in the project directory.
3. Run a client using the following command:

```
python client.py
```

You will be prompted to enter a nickname.

### Connecting from Different Devices

- To connect from different devices on the same network, you'll need the IP address of the machine running the server. Clients can provide this IP address during client setup to connect to the server.

## Features

### Text Chat

Clients can send text messages to the server, which will then be broadcasted to all connected clients.

### File Transfer

Clients can send files to the server, which will be broadcasted to all connected clients. The files are saved in the server's file_folder directory. 
To send a file use the following format:
```
FILE file_path/file_name
```
