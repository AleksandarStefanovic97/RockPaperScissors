from game_functions import print_instructions, get_player_choice, game_round


def main():
    print("Hello! Welcome to Rock, Paper, Scissors!")

    player_score = 0
    computer_score = 0

    while True:
        try:
            choice = int(input("Press 1 for new game, 2 for score, 3 for info or 4 to quit. "))
        except ValueError:
            print("Invalid input! Please enter 1, 2, 3 or 4. ")
            continue

        if choice == 4:
            print("See you later!")
            break

        elif choice == 3:
            print_instructions()

        elif choice == 2:
            print(f"Your score is {player_score} and computer score is {computer_score}.")

        elif choice == 1:
            player_score, computer_score = game_round(player_score, computer_score)

        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
