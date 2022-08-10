############### TicTacToe Project #####################

############### Our TicTacToe Rules #####################
# The gameplay will be as follows.

# First, one user will place their sign in one of the available empty boxes.
# Next, the second user will place their sign in one of the available empty boxes.
# The goal of the players is to place their respective signs completely row-wise or column-wise, or diagonally.
# The game goes on until a player wins the game or it ended up in a draw by filling all boxes without a winning match.

# How does the game work?
# The board is numbered like the keyboard’s number pad. And thus, a player can make their move in the game board by entering the number from the keyboard number pad.
#  7 | 8 | 9
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  1 | 2 | 3

import random


# Create a board using a 2-dimensional array and initialize each element as empty.

def newMove():
    # Ask the user to enter the position number.
    new_spot = int(input(f"{players[turn].name} enter a position number: \n"))
    if new_spot in new_game.free_spots:
        new_game.theBoard[new_spot] = players[turn].symbol
        new_game.free_spots.remove(new_spot)
        players[turn].spots_taken.append(new_spot)
        return
    else:
        print("That is not a valid choice! Try again.")
        newMove()


class TicTacToe:

    def __init__(self):
        self.theBoard = {7: ' ', 8: ' ', 9: ' ',
                         4: ' ', 5: ' ', 6: ' ',
                         1: ' ', 2: ' ', 3: ' '}

        self.free_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def printBoard(self):
        print(f" {self.theBoard[7]} | {self.theBoard[8]} | {self.theBoard[9]}")
        print('---+---+---')
        print(f" {self.theBoard[4]} | {self.theBoard[5]} | {self.theBoard[6]}")
        print('---+---+---')
        print(f" {self.theBoard[1]} | {self.theBoard[2]} | {self.theBoard[3]}\n\n")


class Player:
    def __init__(self, name, symbol):
        self.spots_taken = []
        self.name = name
        self.symbol = symbol


def newMove():
    # If a one player game and it is the computers move, then it will choose randomly from the free spots
    if no_of_players == 1 and turn == 1:
        new_spot = random.choice(new_game.free_spots)
    else:
        # Ask the user to enter the position number.
        new_spot = int(input(f"{players[turn].name} enter a position number: \n"))

    if new_spot in new_game.free_spots:
        new_game.theBoard[new_spot] = players[turn].symbol
        new_game.free_spots.remove(new_spot)
        players[turn].spots_taken.append(new_spot)
        return
    else:
        print("That is not a valid choice! Try again.")
        newMove()


# Check whether the current player won the game or not.
def isPlayWin():
    winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal win
                      [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical win
                      [1, 5, 9], [3, 5, 7]]  # diagonal win
    check_list = players[turn].spots_taken
    items = set(check_list)
    return sum([set(combo).issubset(items) for combo in winning_combos])


def start_game():
    global turn
    is_game_over = False
    new_game.printBoard()

    # Write an infinite loop that breaks when the game is over (either win or draw).
    while not is_game_over:
        newMove()
        # If the current player won the game, then print a winning message and break the infinite loop.
        if isPlayWin():
            print(f"Player {players[turn].name} wins!")
            print("Game Over")
            is_game_over = True

        # Check whether the board is filled or not.
        # If the board is filled, then print the draw message and break the infinite loop.
        elif len(new_game.free_spots) == 0:
            print("It's a draw! Game Over.")
            is_game_over = True
        else:
            turn = 1 - turn
            print(f'inside isPlayWin: {turn}')
        new_game.printBoard()


while input("Do you want to play a game of TicTacToe? Type 'y' or 'n': ") == "y":
    new_game = TicTacToe()
    no_of_players = int(input("How many players are there? Type '1' or '2': "))

    player_one = Player("Player One", "X")
    player_two = Player("Player Two", "O")
    players = [player_one, player_two]
    turn = 0
    start_game()

# Show the board to the user to select the spot for the next move.

# Finally, show the user the final view of the board.

# Select one or two player game
if __name__ == '__main__':
    start_game()
