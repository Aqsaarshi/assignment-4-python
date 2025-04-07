import random 
def main():
    #Generate the secret number at random 
    secret_num : int = random.randint(1,99)

    print("I am thinking of a number between 1 and 99...")

    #Get user's guess
    guess = int(input("Enter a guess: "))

    while guess != secret_num:
        if guess < secret_num: 
            print("Your guess is too low")

        else:
            print("Your is too high")

        print()
        guess: int = int(input("Enter a new guess: "))

    print("Congrats! The number was: " + str(secret_num)) 

if __name__ == "__main__":
    main()               