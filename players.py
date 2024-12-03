import PySimpleGUI as sg
from db_connection import *
connection = create_connection("C:\\school\\CS 361 - software\\sqLite\\my_database.sqlite")


def players():
    while True:
        user_input = input("**************************************************************************************\n"
                           "--Enter a username to view the stats of a player.  \n"
                           "--Enter 's' to select a player username from a list of all users and view their stats\n"
                           "--Enter 'm' to go back to the main menu \n"
                           "**************************************************************************************\n")

        if user_input == 'm':
            return

        if user_input == 's':
            user_input = gui_display()

        # Use the existing connection to execute queries
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
        result = cursor.fetchone()
        cursor.close()  # Close the cursor after executing the query

        if result:
            username = result[1]
            games_played = result[3]
            wins = result[4]
            losses = result[5]
            win_rate = result[6]
            win_rate_rounded = 100 * (round(result[6], 2))


            # Print the values
            print("------------------------------------------\n")
            print(f"       {username}  Stats:   ")
            print("------------------------------------------\n")
            print(f"Username: {username} ")
            print(f"Games Played: {games_played}")
            print(f"Wins: {wins}")
            print(f"Losses: {losses}")
            print(f"Win Rate: {win_rate_rounded}%\n")

            while True:
                new_input = input("******************************************\n"
                                  "--Enter 'm' To go back to the main menu\n"
                                  "--Enter '1' to search for another player \n"
                                  "--Enter '2' to delete this player\n"
                                  "*******************************************\n")
                if new_input == 'm':
                    return "m"
                elif new_input == '1':
                    break

                elif new_input == '2':
                    password = input("*************************************************************\n"
                                     "--Enter the password for this account to delete this player\n"
                                     "*************************************************************\n")
                    if password == result[2]:
                        delete_user(username)
                    else:
                        print("Password is incorrect.\n")
                        continue
                else:
                    print("You entered an invalid response.\n")


        else:
            print("Username does not exist.\n")

def gui_display():
    c = connection.cursor()

    # Retrieve users from the database
    c.execute("SELECT username FROM users")
    usernames = c.fetchall()

    # Define layout for PySimpleGUI window
    layout = [
        [sg.Text("Select a user:")],
        [sg.Listbox(values=[user[0] for user in usernames], size=(30, 10), key='-USER LIST-')],
        [sg.Button("OK")]
    ]

    # Create the PySimpleGUI window
    window = sg.Window("User List", layout)

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "OK":
            break

    # Close the window
    window.close()
    # Return the selected user
    return values['-USER LIST-'][0] if values['-USER LIST-'] else None


def delete_user(username):
    # Define the layout of the popup
    layout = [
        [sg.Text('Are you sure you want to delete this player? \n'
                 'This permanently deletes user account and stats. \n'
                 'This cannot be undone. ')],
        [sg.Button('Confirm.')],
        [sg.Button('Cancel.')]
    ]

    # Create the modal window
    window = sg.Window('Modal Popup', layout, modal=True, location= (100,100))

    # Read events and handle button clicks
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel.':
            window.close()
            break
        if event == 'Confirm.':
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE username = ?", (username,))

            connection.commit()
            cursor.close()
            print(f"{username} has been deleted.")
            window.close()
            break

    # Close the window when the user clicks OK
    window.close()
    return
