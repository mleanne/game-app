def new():
    print("*************************************************************\n"
          "The games Mancala and Tic Tac Toe have been added to the \n"
          "games section! You are able to try out a new game and play\n"
          "as 1 player against the computer, or 2 player with a friend. \n"
          "*************************************************************\n\n")
    while True:
        user_input = input("*****************************************\n"
                           "--Enter 'm' to go back to the main menu: \n"
                           "*****************************************\n")
        if user_input == 'm':
            return
        else:
            print("Uh Oh! You entered an invalid response. \n")
            continue