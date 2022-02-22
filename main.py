def main():
    
    # Get players' names
    global name1 
    name1 = input("Player 1, what is your name? \n")
    print(f"\nHello {name1}!")
    
    global name2
    name2 = input("Player 2, what is your name? \n")
    while name2 == name1:
      print("\nPlayer names must be different")
      name2 = input("Player 2, what is your real name? \n")
    print(f"\nHello {name2}!")
    
    # Definitions
    global board_size
    global connection
    global BOARD
    BOARD = []
    COLUMN_OPTIONS = []
    BOARD_OPTIONS = [5, 7, 9]

    # Get valid user input about board size
    board_innacuracy = True
    while board_innacuracy == True:
        board_size = input("What size board would you like? 5, 7, or 9 \n")
        
        try:
            board_test = int(board_size)
        except ValueError:    
            board_size = 11
                
        if int(board_size) in BOARD_OPTIONS:
            board_innacuracy = False
            board_size = int(board_size)
        else:
            print("Please type only an integer.")
    
    # Number of tokens in a row needed to win
    connection = (board_size + 1) / 2
    
    # Introduce game to user
    print(f"\nThe board is {board_size} x {board_size}")
    print(f"You need {int(connection)} in a row to win!")
    
    # Create column options based on board size
    for columns in range(board_size):
        COLUMN_OPTIONS.append(columns + 1)
    
    # Set up board
    for row in range(board_size):
        BOARD.append([])
    for row in range(board_size):    
        for column in range(board_size):
            BOARD[column].append(u"\U000026AA")
    
    display_board()
        
    current_player = name1
    
    while True:
        
        # token color is blue or red
        if current_player == name1:
            token = u"\U0001F535"
            token_color = "blue"
        else: 
            token = u"\U0001F534"
            token_color = "red"
        
        # Test for correct integer user input
        input_innacuracy = True
        while input_innacuracy == True:
            drop_column = input(f"\n{current_player}'s turn to play {token_color}. Choose a column: ")
        
            try:
                column_test = int(drop_column)
            except ValueError:    
                drop_column = board_size + 1
                
            if int(drop_column) in COLUMN_OPTIONS:
                input_innacuracy = False
            else:
                print(f"You must choose one of the following integers: {COLUMN_OPTIONS}")
                
        drop_column = float(drop_column)
        drop_column = int(drop_column - 1)
        
        # Check if column is full
        if BOARD[0][drop_column] != u"\U000026AA":
            print("\nColumn is full. Pick another column.")
            current_player = change_player(current_player)
        
        # Add colored token to the board    
        else:
            for row in range((board_size - 1), -1, -1):
                if BOARD[row][drop_column] == u"\U000026AA":
                    BOARD[row][drop_column] = token
                
                    # Display board
                    display_board()
                    break
                
        # Check to see if this move creates a winner
        winner = check_winner()
        
        # Print winner and end game if winner is found
        if winner == True:
            print(f"\n{current_player} wins!")
            print("Let's play again!\n")
            main()
        else:
            current_player = change_player(current_player)
        
        # Check for a full board resulting in a tie
        for row in range(board_size):
            if u"\U000026AA" in BOARD[row]:
                break
                    
            print("Tie Game!")
            return


# Prints out the current board
def display_board():
    print("\n")
    for row in range(board_size):
        print(*BOARD[row], sep="")


# Checks for a winner after each move
def check_winner():
    
    temp_list = [0] * int(connection)
    
    # horizontal winner check
    for row in range(board_size):
        for column in range(int(connection)):
            for i in range(int(connection)):
                temp_list[i] = BOARD[row][column + i]
        
            winner_found = check_connection(temp_list)
            if winner_found == True:
                return True
     
    # vertical winner check
    for column in range(board_size):
        for row in range(int(connection)):
            for i in range(int(connection)):
                temp_list[i] = BOARD[row + i][column]
        
            winner_found = check_connection(temp_list)
            if winner_found == True:
                return True
    
    # diagonal southeast winner check
    for row in range(int(connection)):
        for column in range(int(connection)):
            for i in range(int(connection)):
                temp_list[i] = BOARD[row + i][column + i]
            
            winner_found = check_connection(temp_list)
            if winner_found == True:
                return True
                    
    # diagonal southwest winner check
    for row in range(int(connection)):
        for column in range((board_size - 1), (board_size - int(connection) - 1), -1):
            for i in range(int(connection)):
                temp_list[i] = BOARD[row + i][column - i]
            
            winner_found = check_connection(temp_list)
            if winner_found == True:
                return True

    return False


# Switch turns for players
def change_player(player):
    if player == name2:
        player = name1
    else: 
        player = name2
    return player


# Check to see if the temporary list of four dots are all red or all blue
def check_connection(possible_connection):
    if possible_connection[0] != u"\U000026AA":
        if possible_connection.count(possible_connection[0]) == len(possible_connection):
            return True
    else:
        return False
 
        
if __name__ == "__main__":
    main()