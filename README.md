# Python Hangman (Text-Based)

A lightweight, terminal-based Hangman game written in Python. This project is built using basic programming constructs, making it an excellent resource for learning Python fundamentals.

## Features

- **Random Word Selection**: Randomly selects one word from a predefined list of 5 words at the start of each game.
- **Input Validation**: Ensures player guesses are single alphabetical characters and prevents penalties for duplicate guesses.
- **Visual Word State Tracker**: Shows the word's current state (e.g., `_ p p _ e`) after each guess.
- **Attempt Tracking**: Tracks and displays already guessed letters and remaining incorrect attempts.
- **Winning/Loss Endings**: Displays congratulations on success, or reveals the secret word on failure.
- **Pure Python**: Implemented without any external packages—only uses Python's built-in tools.

## Requirements & Constraints

This implementation strictly uses:
- The standard `random` library
- Core control structures (`while` loop, `if-else` conditionals)
- Basic data structures (Strings, Lists)
- No graphics or audio (100% console input/output)

## How to Run

Ensure you have Python installed on your system. Run the game via your terminal:

```bash
python hangman.py
```

## How to Play

1. Run the game in your console.
2. The game will display the mystery word as underscores (e.g., `_ _ _ _ _`).
3. Enter one letter at a time when prompted.
4. You have up to 6 incorrect attempts before the game ends.
5. Guess the entire word correctly to win!
