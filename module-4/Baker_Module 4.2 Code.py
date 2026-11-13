# Mariana Baker, Module 4.2 Assignment, 1/13/26
# The program reads 2018 Sitka weather data from a CSV file and presents an interactive menu allowing the user to plot daily high temperatures in red, daily low temperatures in blue, or exit the program.
import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Open and read weather data
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Program loop with menu instructions
while True:
    print("\n--- Sitka Weather Menu ---")
    print("Enter 'highs' to view daily high temperatures")
    print("Enter 'lows' to view daily low temperatures")
    print("Enter 'exit' to quit the program")

    choice = input("Select an option (highs/lows/exit): ").strip().lower()

    if choice == 'highs':
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == 'lows':
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == 'exit':
        print("\nThank you for using the Sitka Weather program. Exiting...")
        sys.exit()

    else:
        print("\nInvalid selection. Please enter 'highs', 'lows', or 'exit'.")