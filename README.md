# COMP9001_finalproject

## Word Guessing Game

Welcome to the Word Guessing Game! This is a classic "Hangman"-style game where you try to guess a secret word one letter at a time. The game is built using fundamental programming concepts like input, conditionals, loops, and functions, making it a great example for learning and applying these core skills.
How to Play

    Choose a Topic: When you start the game, you'll be presented with a list of diverse topics like Movies, Books, Sports, Animals, Food, and more. Select the category you want to guess from.
    Guess the Word: A secret word from your chosen topic will be randomly selected. You'll see a series of underscores representing the letters of the word (e.g., _ _ _ _ _).
    Enter Your Guess: Type a single letter as your guess.
        If your guess is correct, the letter will be revealed in all its correct positions in the word.
        If your guess is incorrect, a part of the hangman figure will be drawn. You have a total of 8 wrong guesses before the game ends!
    Hints: You can type hint once per game to get one correct, unguessed letter revealed. Use it wisely!
    Win or Lose:
        You win if you correctly guess all the letters in the word before running out of attempts.
        You lose if the hangman figure is fully drawn (after 8 wrong guesses).
    Play Again: After each round, you'll be asked if you want to play another game.

## Game Features

    Diverse Word Banks: The game includes a wide variety of topics, each with a rich collection of words, ensuring a fresh experience every time you play.
    Clear Visual Feedback: As you make guesses, the hangman figure progresses, providing a clear visual indicator of your remaining attempts. Correct guesses fill in the word, showing your progress.
    Limited Attempts: Players have 8 attempts to guess the word, adding a challenge to each round.
    Single Hint: A one-time hint feature is available per game to help you out when you're stuck.
    User-Friendly Interface: Simple text-based prompts guide you through the game, making it easy to understand and play.

## Technical Details

The game is implemented in Python and leverages the following:

    Dictionaries (TOPICS, TOPIC_DESCRIPTIONS): Used to organize word banks and their descriptions by topic.
    Lists (HANGMAN_PICS): Stores the ASCII art for each stage of the hangman figure.
    Sets (guessed_letters): Efficiently tracks letters already guessed by the player, preventing duplicate guesses.
    random module: Used to select a random topic and a random word from the chosen topic.
    Functions: The code is modularized into functions (choose_topic, choose_word, display_word, get_hint, word_guessing_game) to improve readability and maintainability.
    Control Flow: while loops manage the game flow, and if/elif/else statements handle user input and game logic.

## Project Notes

This game was initially conceived as a final project for COMP9001, aiming to demonstrate proficiency in fundamental Python programming concepts. The design emphasizes clear user interaction, visual feedback, and replayability through varied word banks.
