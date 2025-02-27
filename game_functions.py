import random

def print_instructions():
    print("Rock, Paper, Scissors is a game where rock beats scissors, scissors beats paper, and paper beats rock.")


def get_player_choice():
    try:
        return int(input("Type 1 for rock, 2 for paper, 3 for scissors or 4 to quit. "))
    except ValueError:
        print("Invalid input! Please type a number between 1 and 4. ")
        return None


def game_round(player_score, computer_score):
    while True:
        player_pick = get_player_choice()

        if player_pick == 4:
            return player_score, computer_score

        if player_pick is None or player_pick not in [1, 2, 3]:
            print("Invalid input! Please enter 1, 2, 3 or 4. ")
            continue

        computer_pick = random.randint(1, 3)
        print(f"Computer chose {computer_pick}.")

        if player_pick == computer_pick:
            print("Draw!")

        elif (player_pick == 1 and computer_pick == 3) or (player_pick == 2 and computer_pick == 1) or (
                player_pick == 3 and computer_pick == 2):
            print("You win!")
            player_score += 1

        else:
            print("Computer wins!")
            computer_score += 1

        return player_pick, computer_pick
