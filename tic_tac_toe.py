# tic_tac_toe.py
# Player (X) vs computer (O). The computer picks random empty squares.
# Run it with:  python tic_tac_toe.py

import random

# Every possible three-in-a-row, using square positions 0-8:
#
#    0 | 1 | 2
#   ---+---+---
#    3 | 4 | 5
#   ---+---+---
#    6 | 7 | 8
#
WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def show_board(board):
    """Print the board in a 3x3 grid."""
    print()
    for row in range(3):
        start = row * 3
        print(" " + " | ".join(board[start:start + 3]))
        if row < 2:
            print("---+---+---")
    print()


def get_empty_squares(board):
    """Return a list of the positions (0-8) that haven't been taken yet."""
    empty = []
    for position in range(9):
        if board[position] not in ("X", "O"):
            empty.append(position)
    return empty


def get_player_move(board):
    """Ask the player for a square, and keep asking until it's valid."""
    while True:
        choice = input("Pick a square (1-9): ").strip()

        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please type a number from 1 to 9.")
            continue  # skip the rest and ask again

        position = int(choice) - 1  # players count 1-9, Python counts 0-8
        if board[position] in ("X", "O"):
            print("That square is taken. Try another.")
            continue

        return position


def find_completing_move(board, mark):
    """If `mark` has two in a line and the third square is empty,
    return that empty square. Otherwise return None."""
    for line in WINNING_LINES:
        count = 0
        empty_spot = None
        for position in line:
            if board[position] == mark:
                count += 1
            elif board[position] not in ("X", "O"):
                empty_spot = position
        if count == 2 and empty_spot is not None:
            return empty_spot
    return None


def line_is_open(board, line):
    """A line is still open to the computer if the player hasn't claimed any of it."""
    for position in line:
        if board[position] == "X":
            return False
    return True


def get_computer_move(board):
    """Choose a move: win if possible, block if necessary,
    otherwise take the square on the most lines still open."""
    # 1. Can I win right now?
    move = find_completing_move(board, "O")
    if move is not None:
        return move
 
    # 2. Does the player need to be blocked?
    move = find_completing_move(board, "X")
    if move is not None:
        return move
 
    # 3. Score each empty square by how many open lines it sits on
    best_score = -1
    best_moves = []
    for position in get_empty_squares(board):
        score = 0
        for line in WINNING_LINES:
            if position in line and line_is_open(board, line):
                score += 1
 
        if score > best_score:
            best_score = score
            best_moves = [position]       # new best: start a fresh list
        elif score == best_score:
            best_moves.append(position)   # tied for best: add to the list
 
    # If several squares tie, pick one of them at random
    return random.choice(best_moves)




def find_winner(board):
    """Return 'X' or 'O' if someone has three in a row, otherwise None."""
    for a, b, c in WINNING_LINES:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None


def main():
    # Empty squares hold their own number, so the player can see what to type
    board = list("123456789")
    current = "X"  # the player always goes first

    print("Welcome to Tic-Tac-Toe! You are X, the computer is O.")

    while True:
        show_board(board)

        if current == "X":
            position = get_player_move(board)
        else:
            position = get_computer_move(board)
            print(f"The computer takes square {position + 1}.")

        board[position] = current

        winner = find_winner(board)
        if winner:
            show_board(board)
            if winner == "X":
                print("You win!")
            else:
                print("The computer wins!")
            break

        if not get_empty_squares(board):
            show_board(board)
            print("It's a tie!")
            break

        # Switch turns
        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    main()