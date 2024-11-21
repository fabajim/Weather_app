import socket
import os
from dotenv import load_dotenv
import json
import requests

HOST = 'localhost'
PORT = 8000
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_response():
    server = socket.socket()
    server.bind((HOST, PORT))

    server.listen(2)
    connect, address = server.accept()
    data = connect.recv(1024).decode()

    print("Received message: ", data)
    url = BASE_URL + "appid=" + API_KEY + "&q=" + data
    res = requests.get(url).json()
    res = json.dumps(res)
    print("sending: ", res)

    connect.send(res.encode())
    connect.close()


if __name__ == '__main__':
    while True:
        get_response()