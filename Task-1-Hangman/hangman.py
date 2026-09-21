import random

# List of 5 predefined words
words = ["python", "coding", "computer", "program", "student"]

# Choose a random word from the list
word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Number of incorrect guesses
wrong_guesses = 0

# Maximum allowed incorrect guesses
max_wrong_guesses = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses available.")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the complete word
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Ask the player for a letter
    guess = input("Enter a letter: ").lower()

    # Check whether the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess to the guessed letters list
    guessed_letters.append(guess)

    # Check whether the guessed letter is in the word
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

    # Display remaining attempts
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

# If the player uses all 6 incorrect guesses
else:
    print("\n💀 GAME OVER!")
    print("You used all 6 incorrect guesses.")
    print("The correct word was:", word)

print("\nThank you for playing!")