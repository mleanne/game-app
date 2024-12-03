import socket
from mancala import *
from mancala1 import *
from tic_tac_toe2 import *
from tic_tac_toe1 import *
from tutorials import tic_tutorial, mancala_tutorial
from db_connection import *
connection = create_connection("C:\\school\\CS 361 - software\\sqLite\\my_database.sqlite")


def choose_game():
    while True:

        print("       Game selection Menu  \n")
        print('-----------------------------')
        print("1----- mancala ")
        print("2----- mancala tutorial")
        print("3----- Tic Tac Toe")
        print("4------Tic tac toe tutorial")

        user_input = input("******************************************************\n"
                           "--Enter a number to choose one of the options above\n"
                           "--Enter 'b' to go back and change players'. \n"
                           "--Enter 'm' to go back to the main menu\n"
                           "*******************************************************\n")
        if user_input == "m":
            return "m"
        if user_input == 'b':
            return
        elif user_input == '1':
            return 'mancala'
        elif user_input == '2':
            mancala_tutorial()
        elif user_input == '3':
            return "tic"
        elif user_input == '4':
            tic_tutorial()
        else:
            print("Input invalid. \n")


def start_game(player_1, player_2, game):
    """Initiates specific game chosen on play_setup menu"""
    if game == 'mancala':
        if player_2 == "computer":
            start_mancala1(player_1)
        else:
            start_mancala(player_1, player_2)


    elif game == 'tic':
        if player_2 == "computer":
            start_1_tic(player_1)
        else:
            start_tic(player_1, player_2)


def start_1_tic(player):
    """Starts the instance of 1 player tic tac toe"""
    while True:
        game = TicTacToe1(player)
        if game.get_exit():
            break
        elif game.get_tie():
            update_loser(player)
            print("Tie Game!")
        else:
            update_loser(game.get_loser())
            update_winner(game.get_winner())
            print(player, "Wins!")
        break


def start_tic(player1, player2):
    """Starts the instance of 2 player tic tac toe"""
    while True:
        game = TicTacToe2(player1, player2)
        if game.get_exit():
            break
        elif game.get_tie():
            update_loser(player1)
            update_loser(player2)
            print("Tie Game!")
        else:
            update_loser(game.get_loser())
            update_winner(game.get_winner())
            print(game.get_winner(), "Wins!")
        break

def start_mancala1(player):
    """starts an instance of 1-player mancala"""
    while True:
        game = Mancala1(player)
        if game.get_exit():
            break
        elif game.get_tie():
            update_loser(player)
            print("Tie game!")
        else:
            update_loser(game.get_loser())
            update_winner(game.get_winner())
            print(game.get_winner(), "Wins!")
        break


def start_mancala(player_1, player_2):
    """starts the instance of mancala to play"""
    while True:
        game = Mancala(player_1, player_2)
        if game.is_game_over():
            if game.get_tie():       # game is over bc players tied
                update_loser(player_1)
                update_loser(player_2)
                break
            elif game.get_winner():   # game is over bc player won
                update_winner(game.get_winner())
                update_loser(game.get_loser())
                break
            break  # game is over bc player exited


def update_winner(username):
    # dont keep stats for computer
    if username == 'computer':
        return

    cursor = connection.cursor()

    try:
        # Execute the UPDATE statement
        cursor.execute("""
                UPDATE users
                SET 
                    games_played = games_played + 1,
                    wins = wins + 1,
                    win_rate = (wins + 1.0) / (games_played + 1)
                WHERE
                    username = ?
            """, (username,))

        # Commit the transaction to save changes to the database
        connection.commit()
    except Exception as e:
        print(f"Error updating user: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
    return


def update_loser(username):
    if username == 'computer':
        return

    cursor = connection.cursor()

    try:
        # Execute the UPDATE statement
        cursor.execute("""
                    UPDATE users
                    SET 
                        games_played = games_played + 1,
                        losses = losses + 1,
                        win_rate = (wins) / (games_played + 1.0)
                    WHERE
                        username = ?
                """, (username,))

        # Commit the transaction to save changes to the database
        connection.commit()
    except Exception as e:
        print(f"Error updating user: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
    return



