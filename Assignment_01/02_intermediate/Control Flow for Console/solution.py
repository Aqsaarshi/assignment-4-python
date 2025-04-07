import random

NUM_ROUNDS = 5

def main():
    score = 0
    print("Welcome To the High-Low Game!🤯")

    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_number}")

        # Generate a random number for the user (1 to 100)
        user_number = random.randint(1, 100)

        # Generate a random number for the computer (1 to 100)
        computer_number = random.randint(1, 100)

        # Show the user their number
        print(f"Your number is {user_number}")

        # Ask the user to guess if their number is higher or lower
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Ensure the user enters a valid input
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").strip().lower()

        # Check if the guess is correct
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! 🤩 The computer's number was {computer_number}")
            score += 1
        else:
            print(f"AWW🥹, That's incorrect. The computer's number was {computer_number}")    

        # Output the current score
        print(f"Your score is now {score}")

    # Game over, print the final score and conditional messages
    print("\nThanks for playing!")
    if score == NUM_ROUNDS:
        print("WOW YOU PLAYED PERFECTLY DUDE! 🤩")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well! 😄")
    else:
        print("peww Better luck next time!☺️")

if __name__ == "__main__":
    main()
