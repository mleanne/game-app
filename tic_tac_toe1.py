import copy
import socket

class TicTacToe1:
    """Defines an instance of the game tic tac toe for 1 player against the computer"""

    def __init__(self, name_1):
        self._player1 = name_1
        self._player2 = "computer"
        self._board = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None,
                       '9': None}
        self._winner = None  # will be set to winner
        self._loser = None
        self._1_turn = True  # describes if it's player A's turn. Used to keep track of whose turn it is
        self._game_over = False  # if game is still in session, will be set to false
        self._tie = False
        self._exit = False
        print("                                     Welcome to Tic tac toe! ")
        print("  ")
        print("     You are playing against the computer. The game board has 9 spaces numbered 1 through 9 with a row of 3 on top,")
        print("3 in the middle, and 3 in the bottom row. You will mark Xs and the computer will mark Os until one or the")
        print("other achieves three in a row of either Xs or Os. They can be counted vertically, horizontally, or diagonally.")
        print("In the event that all spaces are filled and neither player has achieved 3 in a row, the game will end in a tie")
        print(name_1 + " goes first and will enter a number 1-9 for the space they would like to put their X. You can ")
        print("exit the game at any time by entering 'exit' on your turn.")
        self.print_map()
        while True:
            if self._1_turn:
                player = name_1
            else:
                player = 'computer'
            if player != 'computer':
                x = input(player + " enter your move: ")
                if x == 'exit':  # exit game
                    self._exit = True
                    break
                elif not x.isdigit():  # invalid response
                    print("Input invalid. Need an integer")
                    continue
                else:
                    if int(x) > 9 or int(x) < 1:
                        print("Enter a number 1-9")
                        continue
                    if self._board[x]:
                        print('Space occupied. Enter number for an empty space')
                        continue
                    else:
                        self._board[x] = 'X'
                        self.print_board()
                        self.check_board(player)
                        if self._game_over:
                            if self._tie:
                                break
                            self._loser = self._player2
                            break
                        self._1_turn = False
            else:
                x = self.get_num()
                print("computer move:", x)
                if self._board[x]:  # computer gives back a taken space
                    continue
                self._board[x] = 'O'
                self.print_board()
                self.check_board(player)
                if self._game_over:
                    if self._tie:
                        break
                    self._loser = self._player1
                    break
                self._1_turn = True

    def get_tie(self):
        """returns tie status"""
        return self._tie

    def get_winner(self):
        """returns winner"""
        return self._winner

    def get_loser(self):
        """returns loser"""
        return self._loser

    def get_exit(self):
        """returns bool that says whether game was exited early"""
        return self._exit

    def check_board(self, player):
        """checks to see if move ended the game and updates tie, winner, loser accordingly"""
        b = self._board
        # check rows
        if b['1'] == b['2'] and b['2'] == b['3'] and b['1'] != None:
            self._game_over = True
            self._winner = player
            return
        if b['4'] == b['5'] and b['5'] == b['6'] and b['6'] != None:
            self._game_over = True
            self._winner = player
            return
        if b['7'] == b['8'] and b['8'] == b['9'] and b['9'] != None:
            self._game_over = True
            self._winner = player
            return

        # check diagonals
        if b['1'] == b['5'] and b['5'] == b['9'] and b['9'] != None:
            self._game_over = True
            self._winner = player
            return
        if b['3'] == b['5'] and b['5'] == b['7'] and b['7'] != None:
            self._game_over = True
            self._winner = player
            return

        # check columns
        if b['1'] == b['4'] and b['4'] == b['7'] and b['7'] != None:
            self._game_over = True
            self._winner = player
            return
        if b['2'] == b['5'] and b['5'] == b['8'] and b['8'] != None:
            self._game_over = True
            self._winner = player
            return
        if b['3'] == b['6'] and b['6'] == b['9'] and b['9'] != None:
            self._game_over = True
            self._winner = player
            return

        # check tie
        if self.check_tie():
            self._game_over = True

    def check_tie(self):
        """checks if board is all full and we have tie"""
        b = self._board
        if b['1'] and b['2'] and b['3'] and b['4'] and b['5'] and b['6'] and b['7'] and b['8'] and b['9']:
            self._tie = True
            return True

    def print_board(self):
        """Prints the board in a user-friendly way"""
        b = copy.deepcopy(self._board)
        for key in b:
            if b[key] == None:
                b[key] = "*"
        print(f"{b['1']:3} | {b['2']:3} | {b['3']:3}")
        print("---------------")
        print(f"{b['4']:3} | {b['5']:3} | {b['6']:3}")
        print("---------------")
        print(f"{b['7']:3} | {b['8']:3} | {b['9']:3}")

    def print_map(self):
        """Prints a diagram of tic tac toe board with its spaces numbered"""
        print(f"{'1':3} | {'2':3} | {'3':3}")
        print("---------------")
        print(f"{'4':3} | {'5':3} | {'6':3}")
        print("---------------")
        print(f"{'7':3} | {'8':3} | {'9':3}")



    def get_num(self):
        """calls on the micro service server tic_micro and returns a random number"""
        main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main_address = ('localhost', 8100)  # Change to your desired host and port

        try:
            # Connect the socket to the server
            main_socket.connect(main_address)
            # Send the request for random num 1-9
            data = "get"
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
