import random

# Predefined list of exactly 5 words
words = ["python", "keyboard", "computer", "software", "database"]

# Randomly select one word at the start
secret_word = random.choice(words)

# Track guessed letters
guessed_letters = []

# Keep track of incorrect attempts
incorrect_attempts = 0
max_attempts = 6

print("Welcome to Hangman!")
print("Try to guess the secret word. You have 6 incorrect attempts.")

# Main game loop
while incorrect_attempts < max_attempts:
    # Build the current state of the word
    display_word = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append("_")
            
    # Convert state to string for printing
    # E.g., "_ p p _ e" format as requested
    state_str = ""
    for char in display_word:
        state_str += char + " "
    # Remove trailing space
    if len(state_str) > 0:
        state_str = state_str[:-1]
        
    print("\nWord:", state_str)
    
    # Display letters already guessed
    guessed_str = ""
    for char in guessed_letters:
        guessed_str += char + " "
    if len(guessed_str) > 0:
        guessed_str = guessed_str[:-1]
    print("Guessed letters:", guessed_str)
    
    # Check if the word is fully guessed
    word_guessed = True
    for letter in secret_word:
        if letter not in guessed_letters:
            word_guessed = False
            
    if word_guessed:
        print("\nCongratulations! You won! You guessed the word:", secret_word)
        break
        
    # Get user guess
    guess = input("Guess a letter: ").lower()
    
    # Input validation
    if len(guess) != 1:
        print("Please enter exactly one letter.")
    else:
        if not guess.isalpha():
            print("Please enter a valid alphabetical letter.")
        else:
            if guess in guessed_letters:
                print("You have already guessed that letter!")
            else:
                guessed_letters.append(guess)
                if guess in secret_word:
                    print("Correct!")
                else:
                    print("Incorrect!")
                    incorrect_attempts += 1
                    
    # Show remaining incorrect attempts
    print("Remaining incorrect attempts:", max_attempts - incorrect_attempts)

# If attempts run out
if incorrect_attempts == max_attempts:
    print("\nGame over! You lost. The secret word was:", secret_word)
