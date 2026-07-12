import random

words = ["python", "apple", "tiger", "ocean", "chair"]
chosen_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    if all(letter in guessed_letters for letter in chosen_word):
        print("\nCongratulations! You guessed the word:", chosen_word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses == max_wrong_guesses:
    print("\nGame over! The word was:", chosen_word)
