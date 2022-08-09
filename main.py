############### TicTacToe Project #####################

############### Our TicTacToe Rules #####################
# The gameplay will be as follows.

# First, one user will place their sign in one of the available empty boxes.
# Next, the second user will place their sign in one of the available empty boxes.
# The goal of the players is to place their respective signs completely row-wise or column-wise, or diagonally.
# The game goes on until a player wins the game or it ended up in a draw by filling all boxes without a winning match.

import random

# TODO-1 Create a board using a 2-dimensional array and initialize each element as empty.

theBoard = {7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' '}

free_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player = [{"symbol": "X", "spots_taken": []},
          {"symbol": "O", "spots_taken": []}]

turn = 0

def printBoard(board):
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print('---+---+---')
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print('---+---+---')
    print(f" {board[1]} | {board[2]} | {board[3]}\n\n")


def newMove():
    # new_spot = str(random.choice(free_spots))
    new_spot = int(input("Enter the position number: \n"))
    if new_spot in free_spots:
        theBoard[new_spot] = player[turn]["symbol"]
        free_spots.remove(new_spot)
        player[turn]["spots_taken"].append(new_spot)
        print(player[turn]["spots_taken"])
        return
    else:
        print("That is not a valid choice! Try again.")
        newMove()


printBoard(theBoard)
newMove()
turn = 1 - turn

print(free_spots)
print(player[0]["spots_taken"])
print(player[1]["spots_taken"])


printBoard(theBoard)
newMove()
turn = 1 - turn

print(free_spots)
print(player[0]["spots_taken"])
print(player[1]["spots_taken"])

printBoard(theBoard)
newMove()
turn = 1 - turn

print(free_spots)
print(player[0]["spots_taken"])
print(player[1]["spots_taken"])


printBoard(theBoard)




# print(new_spot)
# print(free_spots)
# theBoard[new_spot] = 'X'
# printBoard(theBoard)
#
# new_spot = str(random.choice(free_spots))
# free_spots.remove(new_spot)
#
# print(new_spot)
# print(free_spots)
# theBoard[new_spot] = 'O'
# printBoard(theBoard)
#
# new_spot = input("Choose a position")
# if new_spot in free_spots:
#     free_spots.remove(new_spot)
# else:
#     print("That is not a valid choice! Try again.")
#
# print(new_spot)
# print(free_spots)
# theBoard[new_spot] = 'X'
# printBoard(theBoard)
#
# player_one = []
# player_two = []
#
# printBoard(theBoard)
#
#

# TODO-2 Write a function to check whether the board is filled or not.

# TODO-3 Write a function to check whether a player has won or not.

# TODO-4 Write a function to show the board as we will show the board multiple times to the users while they are playing.

# TODO-5 Write a function to start the game.

# Select the first turn of the player randomly.
# Write an infinite loop that breaks when the game is over (either win or draw).
# Show the board to the user to select the spot for the next move.
# Ask the user to enter the row and column number.
# Update the spot with the respective player sign.
# Check whether the current player won the game or not.
# If the current player won the game, then print a winning message and break the infinite loop.
# Next, check whether the board is filled or not.
# If the board is filled, then print the draw message and break the infinite loop.
# Finally, show the user the final view of the board.

# Select one or two player game
