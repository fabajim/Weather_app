import src
import os

global DEGREES
DEGREES = 'F'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_city(app):
    """Called from main"""
    clear()
    search = 'y'
    while search != 'n' and search != 'N':
        city = input("Please enter a city: ")
        city = city.upper()
        run_city_weather(app, city)
        search = input("Search another city? (y/n): ")
    clear()


def run_city_weather(app, city):
    """called from get_city"""
    app.add_city(city)
    if not app.set_city_data(city):
        print("[Error] ", city, " not found.\n")
        return
    app.display_temps(city, DEGREES)


def get_three_cities(app):
    cities = []
    count = 0
    clear()
    print("Enter Up two three cities\n"
          "Press Enter to leave blank.\n")
    while count < 3:
        city = input("Enter a city: ")
        city = city.upper()
        if len(city) > 0:
            cities.append(city)
        count += 1
    run_three_cities(app, cities)
    input("Press Enter to continue.")
    clear()


def run_three_cities(app, cities):
    for city in cities:
        run_city_weather(app, city)


def view_history(app):
    app.print_cities(DEGREES)
    input("Press Enter to continue.")
    clear()


def change_degree():
    clear()
    global DEGREES
    degree = input("Enter C for celsius or F for fahrenheit (c/f): ")
    if degree == 'c' or degree == 'C':
        DEGREES = 'C'
    else:
        DEGREES = 'F'
    clear()


def get_global_val():
    return DEGREES


def main():
    clear()
    weather_app = src.WeatherApp()
    print("*********************************\n"
          "*  Welcome to the weather app!  *\n"
          "*********************************\n")
    while True:
        print(f'Current Degree Preference is: {DEGREES}\xb0\n')
        print("*****************************************\n"
              "*  Please make a selection              *\n"
              "*  Enter 1 to search of a city          *\n"
              "*  Enter 2 to compare 3 cities          *\n"
              "*  Enter 3 to view session History      *\n"
              "*  Enter 4 to change Degree Preference  *\n"
              "*  Enter 5 to exit                      *\n"
              "*****************************************")
        selection = input("Select a number: ")
        if selection == '1':
            get_city(weather_app)
        elif selection == '2':
            get_three_cities(weather_app)
        elif selection == '3':
            view_history(weather_app)
        elif selection == '4':
            change_degree()
        elif selection == '5':
            break
        else:
            print("[SELECTION ERROR] ", selection, " was invalid.\n")

    print("Thank you, goodbye!")


if __name__ == '__main__':
    main()
