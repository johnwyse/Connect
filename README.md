# Connect
#### Video Demo:  <https://youtu.be/pOx1JPLIpqA>

##### Description:

Connect is a Connect Four-inspired game written in Python and played in the terminal.
Two players enter their names and are then prompted to choose a board size, 5x5, 7x7, or 9x9.
A blank board is then displayed and players take turns choosing columns in which ti "drop" their blue or red tokens.
The game ends when one players gets the needed tokens in a row or if the board fills up without a winner, resulting in a tie.

The program is written in a single file and calls several functions throughout.
In the beginning of the main function, several global variables and lists are declared to set up the board and game parameters.
Names are input by users. Board size is chosen by the user and then "connection" is easily calculated based on the board size.
Connection refers to the number of tokens in a row needed to win the game.

The program checks to make sure a valid board size is chosen: 5, 7, or 9.
At first I only created the game 7x7 before then adding the ability to change the board size.
I also considered giving the user many more board options, but then realized that there was little enjoyment in playing on huge boards.
Boards smaller than 5x5 are also easily won. (Even 5x5 is possible to "break" fairly simply)

Next, the program sets up a list of lists according to board size called BOARD using several loops, and fills each element as a white circle.
Then a function to display the board is called. This was the first part of the game I designed.
The display function removes the spaces and commas usually shown when printing lists.

Next, players alternate back and forth choosing columns in which to drop their tokens. The player's turn and the color of the token alternates.
The program also checks to make sure that a valid integer column is entered each time and that the column is not already full.
After each valid move, a function is called to check for a winner.
This check winner function checks for a winner in four different directions: horizontally, vertically, diagnoally up/right, and diagonally up/left.
If a winner is found, the function returns True, prints the winner, and exits the main function.
If there is no winner, then the next player's turn begins, unless the board is full in which case a tie is printed and the main function is exited.
The changing of turns is a separate function.