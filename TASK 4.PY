import random

def display_choices(user_choice, computer_choice):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def play_round():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Choose your move: rock, paper, or scissors")

    # User input
    user_choice = input("Enter your choice: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice: ").lower()

    # Computer's random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display choices
    display_choices(user_choice, computer_choice)

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

    return result

def main():
    user_score = 0
    computer_score = 0

    while True:
        # Play a round and get the result
        result = play_round()

        # Update the scores
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        # Display current scores
        print(f"\nScores: You - {user_score} | Computer - {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()
