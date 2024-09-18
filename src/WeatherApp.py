import requests
import os
import socket
from dotenv import load_dotenv
from datetime import datetime
from prettytable import PrettyTable


# Set up API
load_dotenv()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv('API_KEY')
HOST = 'localhost'
PORT = 5000


def getData(kelvin):
    """Connects to socket and sends kelvin value to get celsius"""
    try:
        str_kelvin = str(kelvin)
        client = socket.socket()
        client.connect((HOST, PORT))
        client.send(str_kelvin.encode())
        celsius = round(float(client.recv(1024).decode()), 2)
        client.close()
    except ConnectionRefusedError:
        print('Server error, try again later.')
        return
    else:
        return celsius


class City:
    def __init__(self, city) -> None:
        self.city = city
        self.data = self._getResponse()
        # order of temps: current, minimum, maximum
        self.c_temps = []
        self.f_temps = []
        self._convertAndSetTemps()

    def _getResponse(self) -> None:
        url = BASE_URL + "appid=" + API_KEY + "&q=" + self.city
        return requests.get(url).json()

    def getName(self) -> str:
        return self.city

    def _convertAndSetTemps(self) -> tuple:
        cur = self.data['main']['temp']
        low = self.data['main']['temp_min']
        max = self.data['main']['temp_max']
        temps = [cur, low, max]
        for temp in temps:
            temp = getData(temp)
        self.set_c_temps(temps)
        self.set_f_temps()

    def set_c_temps(self, temps) -> None:
        """Insert celsius order: cur, min, max"""
        for val in temps:
            self.c_temps.append(val)

    def set_f_temps(self) -> None:
        """Insert fahrenheit order: cur, min, max"""
        for val in self.c_temps:
            self.f_temps.append((val * 9/5) + 32)

    def get_f_temps(self) -> list:
        return self.f_temps
    
    def get_c_temps(self) -> list:
        return self.c_temps


class WeatherApp:
    def __init__(self, city) -> None:
        self.cities = {}
        self.addCity(city)

    def addCity(self, name) -> None:
        self.cities[name] = City(name)

