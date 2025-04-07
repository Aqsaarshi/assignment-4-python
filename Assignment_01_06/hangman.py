import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left and have used these letters: {' '.join(used_letters)}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Correct!")
            else:
                lives -= 1
                print("❌ Incorrect!")
        elif user_letter in used_letters:
            print("⚠️ You already used that letter.")
        else:
            print("❌ Invalid input.")

    if lives == 0:
        print(f"\n💀 You lost. The word was {word}")
    else:
        print(f"\n🎉 Congrats! You guessed the word {word}!")


# Run the game
hangman()
