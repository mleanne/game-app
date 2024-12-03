from db_connection import *
from tutorials import tutorial
from play_setup import play_setup
from players import players
from scoreboard import scores, view_all
from new import new




def main_menu():

    while True:
        print("----------------------------------------")
        print("                Main Menu:")
        print("----------------------------------------")
        print("1.     Tutorial")
        print("2.     Play")
        print("3.     Scoreboard")
        print("4.     Players")
        print("5.     New\n\n")

        user_input = input("*********************************************************************\n"
                           "--Enter '1' to view the 'Tutorial' and learn more about this program\n"
                           "--Enter a number 2-5 to skip ahead to the rest of the app! \n"
                           "**********************************************************************\n")

        if user_input == '1':
            tutorial()
            continue
        elif user_input == '2':
            play_setup()
            continue
        elif user_input == '3':
            view_all()
            continue
        elif user_input == '4':
            players()
            continue
        elif user_input == '5':
            new()
            continue
        else:
            print("Uh Oh! It looks like you didn't choose an option from the menu!\n "
                  "Please select a number 1-5 or perish. \n")


if __name__ == "__main__":
    # Create a connection to the SQLite database
    # Now you can use the 'connection' object to interact with the database
    connection = create_connection("C:\\school\\CS 361 - software\\sqLite\\my_database.sqlite")
    # create and start lowercase_microservice
    # run main program
    main_menu()






