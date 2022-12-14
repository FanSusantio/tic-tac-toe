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

player = [{"name": "player_one", "symbol": "X", "spots_taken": []},
          {"name": "player_two", "symbol": "O", "spots_taken": []}]

TURN_TOGGLE = 0


def printBoard(board):
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print('---+---+---')
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print('---+---+---')
    print(f" {board[1]} | {board[2]} | {board[3]}\n\n")


def newMove():
    # Ask the user to enter the position number.
    new_spot = int(input(f"{player[TURN_TOGGLE]['name']} enter a position number: \n"))
    # new_spot = str(random.choice(free_spots))
    if new_spot in free_spots:
        theBoard[new_spot] = player[TURN_TOGGLE]["symbol"]
        free_spots.remove(new_spot)
        player[TURN_TOGGLE]["spots_taken"].append(new_spot)
        return
    else:
        print("That is not a valid choice! Try again.")
        newMove()


# Check whether the current player won the game or not.
def isPlayWin():
    winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal win
                      [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical win
                      [1, 5, 9], [3, 5, 7]]  # diagonal win
    check_list = player[TURN_TOGGLE]["spots_taken"]
    items = set(check_list)
    return sum([set(combo).issubset(items) for combo in winning_combos])


def game():
    global TURN_TOGGLE
    is_game_over = False
    printBoard(theBoard)

    # Write an infinite loop that breaks when the game is over (either win or draw).
    while not is_game_over:
        newMove()
        # If the current player won the game, then print a winning message and break the infinite loop.
        if isPlayWin():
            print(f"Player {player[TURN_TOGGLE]['name']} wins!")
            print("Game Over")
            is_game_over = True

        # Check whether the board is filled or not.
        # If the board is filled, then print the draw message and break the infinite loop.
        elif len(free_spots) == 0:
            print("It's a draw! Game Over.")
            is_game_over = True
        else:
            TURN_TOGGLE = 1 - TURN_TOGGLE
        printBoard(theBoard)


game()

# Show the board to the user to select the spot for the next move.

# Finally, show the user the final view of the board.

# Select one or two player game
