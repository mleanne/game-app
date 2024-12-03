from db_connection import *
from players import players
connection = create_connection("C:\\school\\CS 361 - software\\sqLite\\my_database.sqlite")

def scores():
    cursor = connection.cursor()
    print("---------------------------")
    print("       High scores      ")
    print("---------------------------")
    cursor.execute("SELECT * FROM users ORDER BY win_rate DESC LIMIT 5")

    # Fetch all the results
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        win_rate_rounded = round(row[6], 2)
        win_rate_rounded = win_rate_rounded * 100
        print(row[1], "----win rate:", win_rate_rounded, "%")
    print("\n")

    while True:
        choice = input("*********************************************\n"
                       "--Enter 1 to view a specific player's stats \n"
                       "--Enter 'm' to go back to the main menu \n"
                       "**********************************************\n")

        if choice == '1':
            val = players()
            print(val)
            if val == "m":
                return
        if choice == 'm':
            return
        else:
            print("Invalid input. \n")


# replace scores() on main menu with view_all to test database
def view_all():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("All players and their passwords:")
    for row in rows:
        print(row[1]," ", row[2])
    print("\n")
    while True:
        choice = input("********************************************\n"
                       "--Enter 1 to view a specific player's stats \n"
                       "--Enter 'm' to go back to the main menu \n"
                       "*********************************************\n")

        if choice == '1':
            val = players()
            print(val)
            if val == "m":
                return
        if choice == 'm':
            return
        else:
            print("Invalid input. \n")

