from db_connection import *
from games import *
import socket
connection = create_connection("C:\\school\\CS 361 - software\\sqLite\\my_database.sqlite")


def play_setup():

    while True:
        choice = input("*******************************************\n"
                       "--Enter '1' to play against the computer. \n"
                       "--Enter '2' to play with 2 players \n"
                       "--Enter 'm' to go back to the main menu,\n"
                       "*******************************************\n")

        # go back to main menu
        if choice == 'm':
            return

        # two player game
        elif choice == '2':
            player_1 = select_player()
            if player_1 == 'b':
                continue
            if player_1 == 'm':
                return
            player_2 = select_player()
            if player_2 == 'b':
                continue
            if player_2 == 'm':
                return
            game = choose_game()
            if game == 'm':
                return
            if game == 'b':
                continue
            start_game(player_1, player_2, game)
            # game is over and we go back to main menu
            return

        # one player game
        elif choice == '1':
            player_1 = select_player()
            player_2 = 'computer'
            if player_1 == 'b':
                continue
            if player_1 == 'm':
                return
            game = choose_game()
            if game == 'm':
                return
            if game == 'b':
                continue
            start_game(player_1, player_2, game)
            # game is over and we go back to main menu
            return

        else:
            print("Selection invalid. \n")


def select_player():
    while True:

        choice = input("******************************************\n"
                       "--Enter 1 to create an account \n"
                       "--Enter 2 to find an existing account \n"
                       "--Enter 'b' to go back\n"
                       "--Enter 'm' to go back to the main menu \n"
                       "******************************************\n")
        # return to main menu
        if choice == 'm':
            return 'm'
        if choice == 'b':
            return 'b'
        # create new user
        elif choice == '1':
            username = create_account()
            if username == 'm':
                return 'm'
            return username

        # find existing user
        elif choice == '2':
            user_input = input("***************************************************************\n"
                               "--Enter a the username of the account you would like to use.\n"
                               "--usernames are not case-sensitive. \n"
                               "***************************************************************\n")
            # hopefully this calls the microservice
            user_input = lower_case(user_input)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                print(f"You selected account {user_input} \n")
                return user_input
            else:
                print("This username does not exist.")


def create_account():
    while True:
        user_input = input("*************************************************\n"
                           "--Enter a new username to create an account \n"
                           "    The username cannot be 'computer'. Usernames \n"
                           "    are not case sensitive\n"
                           "--Enter 'b' to go back \n"
                           "--Enter 'm' to go back to the main menu\n"
                           "************************************************\n")

        # go back to play_game()
        if user_input == 'b':
            return
        # validate username
        if user_input == 'm':
            return "m"
        elif user_input == 'computer':
            print("Invalid username. \n")
        # check to see if username available
        else:
            # sends data to microservice to change username to all lowercase
            user_input = lower_case(user_input)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                print("This username already exists.")
            else:
                username = choose_password(user_input)
                if username == 'b':
                    break
                return username

def lower_case(data):
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_address = ('localhost', 8000)  # Change to your desired host and port

    try:
        # Connect the socket to the server
        main_socket.connect(main_address)
        # Send the username
        main_socket.sendall(data.encode())

        # Receive the lowercase username
        data = main_socket.recv(1024)
        data = data.decode()

    except Exception as e:
        print("An error occurred:", e)
        data = None

    finally:
        # Clean up the connection
        main_socket.close()

    return data

def password(data):
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_address = ('localhost', 8050)  # Change to your desired host and port

    try:
        # Connect the socket to the server
        main_socket.connect(main_address)
        # Send the username
        main_socket.sendall(data.encode())

        # Receive the lowercase username
        data = main_socket.recv(1024)
        data = data.decode()

    except Exception as e:
        print("An error occurred:", e)
        data = None

    finally:
        # Clean up the connection
        main_socket.close()

    return data


def choose_password(username):
    while True:
        # create password for new account

        option = input("******************************************************\n"
                         "--Enter '1' to generate a random password suggestion\n"
                         "--Enter '2' to create your own password \n"
                         "--Enter 'b' to go back\n"
                         "--Enter 'm' to go back to the main menu \n"
                         "****************************************************\n")
        if option == "1":
            password = gen_password()
            if password == False:
                continue
            else:
                print("Password: ", password)
                break
        elif option == "2":
            password = input("*************************************************\n"
                             "Enter password (password cannot be 'computer'): "
                             "**************************************************\n")
            if password == 'computer':
                print("password Invalid.")
                continue
            print("Password is ", password)
            break
        # returns to create_account
        elif option == 'b':
            return 'b'
        elif option == 'm':
            return 'm'
        else:
            print("Selection invalid.")
            continue
    password = lower_case(password)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE password = ?", (password,))

    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()
    print(f"You have created a new account! Welcome {username}!")
    cursor.close()
    # I think i'm returning to create_account()
    return username

def gen_password():
    """Returns False if user wants to go back without generating a password"""
    while True:
        length = input("***********************************************************************\n"
                       "--Enter a number for the length of the password you want to generate\n"
                       "--Enter 'b' to go back\n"
                       "***********************************************************************\n")
        if length == 'b':
            return False
        if not length.isdigit():
            print("Input invalid.")
        else:
            suggested_password = password(length)   #opens socket
            break
    print("Suggested password: ", suggested_password)
    while True:
        choice = input("***************************************************\n"
                       "Would you like to use the suggested password (y/n)?\n"
                       "****************************************************\n")
        if choice == 'y':
            return suggested_password
        elif choice == 'n':
            return False
        else:
            print("Invalid selection.")







