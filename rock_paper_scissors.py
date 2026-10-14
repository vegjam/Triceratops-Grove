# rock_paper_scissors.py
# A simple player-vs-computer game of Rock, Paper, Scissors.
# Run it with:  python rock_paper_scissors.py

import random  # Python's built-in toolkit for making random choices

# A list of the valid moves
CHOICES = ["rock", "paper", "scissors"]

# A dictionary: each key beats the value it points to
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_player_choice():
    """Ask the player for a move, and keep asking until it's valid."""
    while True:  # loop forever until we 'return' something
        choice = input("Choose rock, paper, or scissors (or 'quit'): ").strip().lower()
        if choice in CHOICES or choice == "quit":
            return choice
        print("Sorry, I didn't understand that. Try again.")


def decide_winner(player, computer):
    """Return 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"
    elif BEATS[player] == computer:
        return "player"
    else:
        return "computer"


def main():
    """Run the game until the player quits."""
    scores = {"player": 0, "computer": 0, "tie": 0}
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        player = get_player_choice()
        if player == "quit":
            break  # exit the loop

        computer = random.choice(CHOICES)
        print(f"You chose {player}. The computer chose {computer}.")

        result = decide_winner(player, computer)
        scores[result] += 1  # add one point to whoever won (or to ties)

        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win this round!")
        else:
            print("The computer wins this round!")

        print(f"Score: You {scores['player']} | Computer {scores['computer']} | Ties {scores['tie']}\n")

    print("Thanks for playing! Final score:", scores)


# This means "only start the game if this file is run directly"
if __name__ == "__main__":
    main()