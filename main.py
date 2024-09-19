# Author: Fabian Jimenez
# Class:  CS361
# Description: Weather app

import src
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_city_weather():
    clear()
    city = input("Please enter a city: ")
    city_weather = src.WeatherApp(city)
    city_weather.displayFTemps(city)
    celsius = input("Enter c to view celsius or enter n to continue. (c/n): ")
    if celsius == 'c' or celsius == 'C':
        city_weather.displayCTemps(city)
    input("Press Enter to continue.")
    clear()


def main():
    clear()
    print("*********************************\n"
          "*  Welcome to the weather app!  *\n"
          "*********************************\n")
    while True:
        print("*********************************\n"
              "*  Please make a selection      *\n"
              "*  Enter 1 to search of a city  *\n"
              "*  Enter 2 to exit              *\n"
              "*********************************")
        selection = input("Select a number: ")
        if selection == '1':
            get_city_weather()
        elif selection == '2':
            break
        else:
            print("[SELECTION ERROR] ", selection, " was invalid.\n")

    print("Thank you, goodbye!")


if __name__ == '__main__':
    main()
