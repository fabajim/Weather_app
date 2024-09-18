import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from prettytable import PrettyTable


# Set up API
load_dotenv()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv('API_KEY')


class WeatherApp:
    def __init__(self) -> None:
        self.response = None
        self.city = None
        self.cities = []
        self.f_temp = None
        self.c_temp = None

    def _getResponse(self) -> None:
        url = BASE_URL + "appid=" + API_KEY + "&q=" + self.city
        self.response = requests.get(url).json()

    def _getFTemp(self) -> float:
        return (self.c_temp * 9/5) + 32

    def setCity(self, city) -> None:
        self.city = city
        self._getResponse()

    def getKTemp(self) -> float:
        return self.response['main']['temp']
    
    def setTemps(self, c_temp):
        self.c_temp = c_temp
        self.f_temp = self._getFTemp()

