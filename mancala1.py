import socket

class Player:
    """Creates a player object for the game Mancala. Initialized in the Mancala class init method."""

    def __init__(self, A_or_B, name):
        self._player = A_or_B
        self._player_name = name
        self._points = 0
        if self._player == "A":
            self._player_route = ['1', '2', '3', '4', '5', '6', 'A', '7', '8', '9', '10', '11', '12']
        else:
            self._player_route = ['7', '8', '9', '10', '11', '12', 'B', '1', '2', '3', '4', '5', '6']

    def get_player(self):
        """Returns "A" or "B" """
        return self._player

    def get_player_name(self):
        """Returns player's name"""
        return self._player_name

    def get_points(self):
        """Returns the number of points player currently has"""
        return self._points

    def update_points(self):
        """Adds 1 to player points when player scores"""
        self._points += 1


class Board:
    """Creates a board object for the game Mancala. Initialized in the Mancala class init method."""

    def __init__(self):
        self._board = {'1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, 'A': 0,
                       '7': 4, '8': 4, '9': 4, '10': 4, '11': 4, '12': 4, 'B': 0}

    def get_board(self):
        """Returns dictionary that represent the game board"""
        return self._board

    def check_side(self, player): # returns true if player side empty, false otherwise
        """Checks to see if all spaces on player's side are empty, if so, the player is allowed to
        move from the other side"""
        if player == 'A':
            if self._board['1'] == 0 and self._board['2'] == 0 and self._board['3'] == 0 and self._board['4'] == 0 and \
                    self._board['5'] == 0 and self._board['6'] == 0:
                return True
            else:
                return False
        if player == 'B':
            if self._board['7'] == 0 and self._board['8'] == 0 and self._board['9'] == 0 and self._board['10'] == 0 and \
                    self._board['11'] == 0 and self._board['12'] == 0:
                return True
            else:
                return False

    def print_board(self, player1, player2):
        """Prints the Mancala board"""
        b = self._board
        print("*************************************************************")
        print(f"                          ", player2, "             ")
        print(f"    {'B':^5} | {'12':^3} | {'11':^3} | {'10':^3} | {'9':^3} | {'8':^3} | {'7':^3} | {'A':^3}")
        print(f"    {'-' * 6}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 6}")
        print(
            f"    {'|':<2} {b['B']:^2} {'|':<2} {b['12']:^2} {'|':<2} {b['11']:^2} {'|':<2} {b['10']:^2} {'|':<2} {b['9']:^2} {'|':<2} {b['8']:^2} {'|':<2} {b['7']:^2} {'|':<2}    {'|':<2}")
        print(f"          {'-' * 6}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 6}")
        print(
            f"    {'|':<2}    {'|':<2} {b['1']:^2} {'|':<2} {b['2']:^2} {'|':<2} {b['3']:^2} {'|':<2} {b['4']:^2} {'|':<2} {b['5']:^2} {'|':<2} {b['6']:^2} {'|':<2} {b['A']:^2} {'|':<2}")
        print(f"    {'-' * 6}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 5}+{'-' * 6}")
        print(f"    {'B':^5} | {'1':^3} | {'2':^3} | {'3':^3} | {'4':^3} | {'5':^3} | {'6':^3} | {'A':^3} ")
        print(f"                          ", player1, "             ")
        print("*************************************************************")

    def is_empty(self, space):
        """Returns true if the space chosen is empty and prompts user to pick another space"""
        if self._board[space] == 0:
            print("This space is empty! Please pick a space with marbles in it. ")
            return True
        else:
            return False



class Mancala1:
    """Defines an instance of the game mancala while initializing the Player class and Board class"""

    def __init__(self, name_1):
        self._playerA = Player("A", name_1)
        self._playerB = Player("B", "computer")
        self._playerA_route = ['1', '2', '3', '4', '5', '6', 'A', '7', '8', '9', '10', '11', '12']
        self._playerB_route = ['7', '8', '9', '10', '11', '12', 'B', '1', '2', '3', '4', '5', '6']
        self._board_object = Board()
        self._winner = None         # will be set to winner
        self._loser = None
        self._a_turn = True         # describes if it's player A's turn. Used to keep track of whose turn it is
        self._game_over = False     # if game is still in session, will be set to false
        self._tie = False
        self._exit = False

        print("                                     Welcome to Mancala! ")
        print("  ")
        print("     You are playing against the computer.The game board has 12 spaces numbered 1 through 12 and two goals")
        print("labeled A and B. Your goal, is is side A and the computer uses side B. Spaces 1-6 are on your side of the \n"
              "board while spaces 7-12 are for the computer. Player A's goal is between spaces 6 and 7 while player B's \n"
              "goal is between 12 and 1.\n"
              "The objective of the game is to have the most marbles in your goal by the time all the spaces are empty \n"
              "     You start the game by choosing a pile of marbles from your side of the board (spaces 1, 2, 3, 4, 5, \n"
              "or 6). Player A will pick up the pile of marbles in their chosen starting space and move in ascending order \n"
              "around the board dropping one marble in each spot until they have no marbles left in their hand. If the last \n"
              "space the player dropped a marble in was not empty, the player will pick up that new pile of marbles and continue \n"
              "around the board. If they landed on an empty space, however, player A's turn is over. If the player lands in \n"
              "their own goal, they can move again from their side of the board. If a player has a turn, and their side of the\n"
              "board is completely empty, they may move from the other player's side of the board. The game is over when there\n"
              "are no marbles left in any of the spaces"
              " Player 1,", name_1 + ", moves first by entering a number for the space to move. \n")
        self._board_object.print_board(name_1, 'computer')
        while True:
            if self._a_turn:
                player = name_1
            else:
                player = "computer"
            if player != 'computer':
                x = input(player + " enter a space: ")
                if x == 'exit':  # exit game
                    self._exit = True
                    break
                elif not x.isdigit():
                    print("Invalid entry. Enter a number for a space on the board")
                    continue
                elif int(x) >= 1 and int(x) <= 6:
                    if self._board_object.is_empty(x):  # if space empty
                        continue
                    if self.move('A', x): # if true, it's player's turn again or game is over
                        self._board_object.print_board(name_1, 'computer')
                        if self._game_over:
                            break
                        continue    # get another move from player if game not over
                    else:
                        self._a_turn = False
                        print("computer will make a move: ")
                        continue
                elif int(x) >= 6 and int(x) <= 12:
                    if self._board_object.check_side("A"):   # returns true if all spaces on their side of board empty
                        if self._board_object.is_empty(x):  # if space empty
                            continue
                        if self.move('A', x):
                            self._board_object.print_board(name_1, 'computer')
                            if self._game_over:
                                break
                            print("You landed in your goal and get to move again.")
                            continue
                        else:
                            self._a_turn = False
                            print("computer will make a move: ")
                            continue
                    else:
                        print("Choose a space on your side of the board")
                        continue
            else:    # player = 'computer'
                x = self.get_random()  # needs to call microservice for number

                if int(x) >= 6 and int(x) <= 12:
                    if self._board_object.is_empty(x):  # if space empty
                        continue
                    if self.move('B', x):  # if true, it's player's turn again or game is over
                        if self._game_over:
                            break
                        continue  # get another move from player if game not over
                    else:
                        self._a_turn = True
                        self._board_object.print_board(name_1, 'computer')
                        continue
                elif int(x) >= 1 and int(x) <= 6:

                    if self._board_object.is_empty(x):  # if space empty
                        continue
                    if self.move('B', x):
                        if self._game_over:
                            break
                        continue
                    else:
                        self._a_turn = True
                        self._board_object.print_board(name_1, 'computer')
                        continue

    def get_winner(self):
        """Returns winner of the game as player object"""
        return self._winner

    def get_loser(self):
        return self._loser

    def get_exit(self):
        """Returns true if game was exited and false otherwise"""
        return self._exit

    def get_random(self):
        """starts client socket to get random number from man_micro. If data is 'same', computer will get number 7-12
        if arg is 'other', computer will get num 1-6. It will return the number"""
        main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main_address = ('localhost', 8075)  # Change to your desired host and port

        try:
            # Connect the socket to the server
            main_socket.connect(main_address)
            # Send the request for random num 1-9
            if self._board_object.check_side('B'):
                data = 'other'
            else:
                data = 'same'

            main_socket.sendall(data.encode())

            # Receive num
            data = main_socket.recv(1024)
            data = data.decode()

        except Exception as e:
            print("An error occurred:", e)
            data = None
        finally:
            # Clean up the connection
            main_socket.close()

        return data


    def move(self, A_or_B, space): #returns true if player turn again, false if next player turn
        """makes move"""
        board = self._board_object.get_board()

        route = self.set_route(A_or_B)

        num_marbles = board[space]  # how many spaces the player can move
        board[space] = 0  # pick up all the marbles in initial space, so it's set to zero
        route_position = route.index(space)  # index of route list
        key = space

        while True:
            while num_marbles != 0:
                if route_position == 12:
                    route_position -= 12
                    key = route[route_position]
                    board[key] += 1
                    num_marbles -= 1
                else:
                    route_position += 1  # move forward one on route list
                    key = route[route_position]
                    self.check_points(key, A_or_B)
                    board[key] += 1
                    num_marbles -= 1
            if board[key] == 1: #lands in an empty space
                break
            else:
                if key != 'B' and key != 'A':
                    num_marbles = board[key]
                    board[key] = 0
                    route_position = route.index(key)
                else:
                    break


        if self.next_turn(A_or_B, key) and not self._game_over: # if true, turn ended and next players turn
            return False

        if self.ends_in_goal(key): # if true,
            return True   # need to check for game over back in move functin right after this returns



    def check_points(self, key, player):
        """Adds 1 point to player's data member self._points"""
        if key == "A" or key == 'B':
            if player == 'A':
                self._playerA.update_points()
            else:
                self._playerB.update_points()


    def set_route(self, player):
        """Sets player route data member"""
        if player == 'A':
            return self._playerA_route
        else:
            return self._playerB_route

    def ends_in_goal(self, space):
        """Returns True if the player ended in their points pile. Returns false, otherwise"""
        board_object = self._board_object
        board = self._board_object.get_board()
        key = space

        if key == 'A' or key == 'B':  # ends in their points pile
            board_object.print_board(self._playerA.get_player_name(), self._playerB.get_player_name())
            if board['A'] == 24 and board['B'] == 24:
                print("Score: A =", board['A'], "B =", board["B"])
                print("IT'S A TIE!")
                self._game_over = True
                self._tie = True
                return True
            elif board['A'] + board['B'] == 48:
                self._winner = self.set_winner()
                print("Score: A =", board['A'], "B =", board["B"])
                print(self._winner, " WINS!")
                self._game_over = True
                return True
            else:
                print("You landed in your own points pile! You go again!")
                return True
        else:
            return False

    def get_tie(self):
        return self._tie

    def next_turn(self, player, space):
        """Returns true if the current turn is over, and it's now the other player's turn. Returns false, otherwise
        Player is 'A' or 'B' while space is an integer"""

        board = self._board_object.get_board()
        key = space

        if board[key] == 1 and key != "A" and key != 'B':  # num_marbles is zero and they ended in a space with zero marbles
            self._board_object.print_board(self._playerA.get_player_name(), self._playerB.get_player_name())
            if player == "A":
                print("You landed in an empty space. ", self._playerB.get_player_name() + "'s turn!")
                self._a_turn = False
            else:
                print("Computer landed in an empty space. ", self._playerA.get_player_name() + "'s turn!")
                self._a_turn = True
            return True
        else:
            return False

    def check_move(self, player, space):
        """Checks to make sure player is starting move on their side of the board"""
        space_num = int(space)
        if player == 'A':
            if space_num <= 6:
                return True
            else:
                return False
        if player == 'B':
            if space_num >= 7:
                return True
            else:
                return False

    def set_winner(self):
        """Sets the winner of the game"""
        board = self._board_object.get_board()

        if board['A'] > board['B']:
            self._loser = self._playerB.get_player_name()
            return self._playerA.get_player_name()
        elif board['A'] < board['B']:
            self._loser = self._playerA.get_player_name()
            return self._playerB.get_player_name()


    def is_game_over(self):
        """Returns True if this game of mancala is over"""
        if self._game_over == True:
            return True
        return False










