import random

total_games = int(input("Best of 1, 3, or 5: "))
print()
win_condition = (total_games + 1) / 2
turn_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

games_played = 0
user_wins = 0
computer_wins = 0
while games_played < total_games:
    print("You  Computer")
    print("", user_wins, "    ", computer_wins)
    user_choice = input("Choose Rock, Paper, Scissors, Lizard, or Spock: ")
    computer_choice = random.choice(turn_options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif user_choice == "Rock":
        games_played += 1
        if computer_choice == "Scissors":
            user_wins += 1
            print("Rock crushes scissors... you win!\n")
        elif computer_choice == "Lizard":
            user_wins += 1
            print("Rock crushes lizard... you win!\n")
        else:
            computer_wins += 1
            print("Computer wins!\n")
    elif user_choice == "Paper":
        games_played += 1
        if computer_choice == "Rock":
            user_wins += 1
            print("Paper covers rock... you win!\n")
        elif computer_choice == "Spock":
            user_wins += 1
            print("Paper disproves Spock... you win!\n")
        else:
            computer_wins += 1
            print("Computer wins!\n")
    elif user_choice == "Scissors":
        games_played += 1
        if computer_choice == "Paper":
            user_wins += 1
            print("Scissors cut paper... you win!\n")
        elif computer_choice == "Lizard":
            user_wins += 1
            print("Scissors decapitates lizard... you win!\n")
        else:
            computer_wins += 1
            print("Computer wins!\n")
    elif user_choice == "Lizard":
        games_played += 1
        if computer_choice == "Spock":
            user_wins += 1
            print("Lizard poisons Spock... you win!\n")
        elif computer_choice == "Paper":
            user_wins += 1
            print("Lizard eats paper... you win!\n")
        else:
            computer_wins += 1
            print("Computer wins!\n")
    elif user_choice == "Spock":
        games_played += 1
        if computer_choice == "Scissors":
            user_wins += 1
            print("Spock smashes scissors... you win!\n")
        elif computer_choice == "Rock":
            user_wins += 1
            print("Spock vaporizes rock... you win!\n")
        else:
            computer_wins += 1
            print("Computer wins!\n")
    
    if user_wins == win_condition:
        print("You have won the best of", total_games, "series!")
        print("You  Computer")
        print("", user_wins, "    ", computer_wins)
        break
    if computer_wins == win_condition:
        print("Computer has won the best of", total_games, "series!")
        print("You  Computer")
        print("", user_wins, "    ", computer_wins)
        break
    

