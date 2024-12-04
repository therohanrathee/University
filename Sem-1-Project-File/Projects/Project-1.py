# Rock Paper Scissors
import random

def get_computer_choice():
    
    # Randomly selects 'Rock', 'Paper', or 'Scissors' for the computer.
    
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_user_choice():
    
    # Prompts the user to select 'Rock', 'Paper', or 'Scissors'.
    # Returns the user's choice if valid, otherwise re-prompts.
    
    while True:
        choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
        if choice in ["Rock", "Paper", "Scissors"]:
            return choice
        print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
   
    # Determines the winner based on user and computer choices.
    # Returns 'User', 'Computer', or 'Tie'.
    
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "User"
    else:
        return "Computer"

def play_game():
    
    # Plays a single round of Rock, Paper, Scissors.
    
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "Tie":
        print("It's a tie!")
    elif winner == "User":
        print("Congratulations! You win!")
    else:
        print("Computer wins! Better luck next time!")

    print("\nThanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
