def tutorial():
    print("********************************************************************\n"
          "                   -----------PLAY----------\n"
          "********************************************************************\n"
          "Under the Play option, you will choose the number of players you'll \n"
          "be playing with (1 or 2), and any new users will be prompted to \n"
          "either create a user account with a password and username or choose \n"
          "to play with an already existing account. You also have the option to \n"
          "prompt the program for password suggestions while making a new account.\n" 
          "Next, you'll choose to read game instructions or choose a game to play.\n"
          "When the game is over, or you choose to exit out, you will be taken \n"
          "back to the main menu.\n"
          "**********************************************************************\n"
          "                   ---------SCOREBOARD-------- \n "
          "**********************************************************************\n"
          "Choosing scoreboard will present a 'scoreboard' of the top 5 (or less \n"
          "depending on on the number of accounts made) players on the app. You \n"
          "see their username and their win rate. From there, you have the option\n"
          "to go back to the main menu or look up a specific player's stats."
          "***********************************************************************\n"
          "                   -----------PLAYERS----------\n"
          "************************************************************************\n"
          "Under the Players option, the user has another way to see the stats for \n"
          "a specific player. From the player's stats page, the user is presented  \n"
          "with the number of games played, the number of wins, the number of losses\n"
          "and the win rate of the selected player. On this page, the user also has \n"
          "the option to delete a player account, provided they also have the \n"
          "password to the account. \n"
          "*************************************************************************\n"
          "                     -----------NEW-----------\n"
          "**************************************************************************\n"
          "The new section highlights any new features or developments on the app. \n"
          "Users should check back periodically to keep up-to-date.\n\n")
    while True:
        user_input = input("*****************************************\n"
                           "--Enter 'm' to go back to the main menu\n"
                           "*****************************************\n")
        if user_input == 'm':
            return
        else:
            print("Uh Oh! You entered an invalid response. \n")


def mancala_tutorial():
    print("**********************************************************************************************************\n"
          "                                 Welcome to the Mancala Tutorial! \n"
          "     This is a two-player game. The game board has 12 spaces numbered 1 through 12 and two goal spots\n"
          "labeled A and B for players A and B, respectively. Spaces 1-6 are on A's side of the board while spaces\n"
          "7-12 are B's side. Player A's goal is between spaces 6 and 7 while player B's goal is between 12 and 1.\n"
          "The objective of the game is to have the most marbles in your goal by the time all the spaces are empty\n"
          "     The Player A starts the game by choosing a pile of marbles from\n"
          "the A side of the board (spaces 1, 2, 3, 4, 5, or 6). Player A will pick up the pile of marbles in their\n"
          "chosen starting space and move in ascending order around the board dropping one marble in each spot until\n"
          "they have no marbles left in their hand. If the last space the player dropped a marble in was not empty,\n"
          "the player will pick up that new pile of marbles and continue around the board. If they landed on an empty\n"
          "space, however, player A's turn is over. If the player lands in their own goal, they can move again from\n"
          "their side of the board. If a player has a turn, and their side of the board is completely empty, they may\n"
          "move from the other player's side of the board. The game is over when there are no marbles left in any of\n"
          "the spaces. An example of an initial board setup is shown below. \n"
          "                '1': 4, '2': 4, '3': 4, '4':  4, '5' : 4, '6' : 4, 'A': 0,                  \n"
          "                '7': 4, '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, 'B': 0\n")


    while True:
        user_input = input("***********************************************\n"
                           "--Enter 'b' to go back to game selection menu\n"
                           "************************************************\n")
        if user_input == 'b':
            return
        else:
            print("Invalid input\n")


def tic_tutorial():

    print("**************************************************************************************************************\n"
          "                                   Welcome to the Tic tac toe Tutorial\n"
          "The game board has 9 spaces numbered 1-9 with a row of 3 on top, 3 in the middle and 3 on the bottom row. \n"
          "Players will take turns marking the board with either Xs or Os until a player has made a line of 3 in a row. \n"
          "This can be counted vertically, horizontally, or diagonally. If neither player has gotten 3 in a row by the \n"
          "time all spaces are filled, the game ends in a tie. \n"
          f"{'1':3} | {'2':3} | {'3':3}\n"
          "---------------\n"
          f"{'4':3} | {'5':3} | {'6':3}\n"
          "---------------\n"
          f"{'7':3} | {'8':3} | {'9':3}")

    while True:
        user_input = input("***************************************\n"
                           "--Enter 'b' to the game selection menu\n"
                           "****************************************\n")
        if user_input == 'b':
            return
        else:
            print("Invalid input\n")
