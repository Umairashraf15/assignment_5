import random

# Constants
NUM_ROUNDS = 5  # You can adjust the number of rounds here

# Welcome message
print("Welcome to the High-Low Game!")
print("--------------------------------")

# Initialize score
score = 0

# Function to get user's valid guess
def get_user_guess():
    while True:
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower()
        if guess in ["higher", "lower"]:
            return guess
        else:
            print("Please enter either 'higher' or 'lower'.")

# Play the game for a set number of rounds
for round_num in range(1, NUM_ROUNDS + 1):
    print(f"\nRound {round_num}")
    
    # Generate numbers for user and computer
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number is {user_number}")
    
    # Get the user's guess
    user_guess = get_user_guess()
    
    # Determine the outcome
    if user_guess == "higher" and user_number > computer_number:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    elif user_guess == "lower" and user_number < computer_number:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    # Print the current score
    print(f"Your score is now {score}")

# End of game summary
print("\nThanks for playing!")
if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
