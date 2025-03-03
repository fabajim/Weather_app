import socket
import json
from prettytable import PrettyTable


HOST = 'localhost'

def get_API_res(city):
    """Microservice - get a JSON API response"""
    try:
        client = socket.socket()
        client.connect((HOST, 8000))
        client.send(city.encode())
        res = client.recv(1024).decode()
        client.close()
    except ConnectionRefusedError:
        print('Server error, try again later.')
        return
    else:
        return res


class City:
    def __init__(self, city) -> None:
        self.city = city
        self.data = None
        # order of temps: current, minimum, maximum
        self.c_temps = []
        self.f_temps = []

    def set_data(self) -> None:
        data = get_API_res(self.city)
        self.data = json.loads(data)

    def get_name(self) -> str:
        return self.city

    def convert_and_set_temps(self) -> None:
        cur = self.data['main']['temp']
        low = self.data['main']['temp_min']
        max = self.data['main']['temp_max']
        temps = [cur, low, max]
        self.set_c_temps(temps)
        self.set_f_temps()

    def set_c_temps(self, temps) -> None:
        """Insert celsius order: cur, min, max"""
        for val in temps:
            c = val - 273.5
            self.c_temps.append(c)

    def set_f_temps(self) -> None:
        """Insert fahrenheit order: cur, min, max"""
        for val in self.c_temps:
            self.f_temps.append((val * 9/5) + 32)

    def get_f_temps(self) -> list:
        return self.f_temps

    def get_c_temps(self) -> list:
        return self.c_temps

    def get_data(self) -> list:
        return self.data
    
    def get_cod(self) -> str:
        return self.data['cod']


class WeatherApp:
    def __init__(self) -> None:
        self.cities = {}

    def add_city(self, name) -> None:
        self.cities[name] = City(name)

    def set_city_data(self, city):
        cur_city = self.cities[city]
        cur_city.set_data()
        cod = cur_city.get_cod()
        if not self.validate_data(cod):
            del self.cities[city]
            return False
        cur_city.convert_and_set_temps()
        return True

    def validate_data(self, data):
        return int(data) < 400

    def display_temps(self, city, degree):
        if degree == 'F':
            self.display_F_temps(city)
        else:
            self.display_C_temps(city)

    def display_F_temps(self, city) -> None:
        f_temps = self.cities[city].get_f_temps()
        self.show_table(f_temps, city, 'F')

    def display_C_temps(self, city) -> None:
        c_temps = self.cities[city].get_c_temps()
        self.show_table(c_temps, city, 'C')

    def show_table(self, temps, city, type) -> None:
        """Uses a table to show temps"""
        table = PrettyTable(['City', 'Current', 'Lows', 'Highs'])
        table.add_row([city, f'{int(temps[0])}{type}\xb0', f'{int(temps[1])}'
                       f'{type}\xb0', f'{int(temps[2])}{type}\xb0'])
        print('\n', table, '\n')

    def print_cities(self, degree):
        """Prints the temps from all cities in cites dict."""
        if not self.cities:
            print("Nothing in search history.")
        for city in self.cities:
            self.display_temps(city, degree)
