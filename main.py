import random

# --- Game Data ---
# Dictionary of topics and corresponding word banks
TOPICS = {
    "movies": [
        "inception", "gladiator", "avatar", "matrix", "interstellar", "godfather", "parasite",
        "dark knight", "shawshank redemption", "pulp fiction", "forrest gump", "titanic",
        "jurassic park", "lion king", "casablanca", "fight club", "spirited away",
        "parasite", "jaws", "back to the future", "toy story", "finding nemo", "superman",
        "the prestige", "avengers", "spiderman"
    ],
    "books": [
        "harry potter", "hobbit", "pride and prejudice", "gatsby", "dracula",
        "frankenstein", "moby dick", "war and peace", "to kill a mockingbird",
        "brave new world", "the odyssey", "crime and punishment", "les miserables",
        "don quixote", "the count of monte cristo", "alice in wonderland",
        "the chronicles of narnia", "the lord of the rings", "enders game",
        "the catcher in the rye"
    ],
    "sports": [
        "soccer", "basketball", "cricket", "tennis", "badminton", "rugby", "baseball",
        "formula one", "ice hockey", "volleyball", "swimming", "boxing", "golf",
        "american football", "cycling", "athletics", "gymnastics", "skiing",
        "snowboarding", "surfing", "table tennis", "wrestling", "judo", "karate"
    ],
    "technology": [
        "artificial intelligence", "cybersecurity", "cloud computing", "blockchain",
        "quantum computing", "virtual reality", "machine learning", "big data",
        "robotics", "augmented reality", "neural network", "cryptography",
        "data science", "web development", "mobile app", "internet of things",
        "biometrics", "nanotechnology", "supercomputer"
    ],
    "history": [
        "world war", "industrial revolution", "ancient egypt", "renaissance",
        "cold war", "american revolution", "french revolution", "roman empire",
        "middle ages", "stone age", "pyramids", "great wall", "viking age", "space race", 
        "civil rights movement", "mesopotamia", "greek mythology", "prehistoric", 
        "colonialism", "enlightenment"
    ],
    "animals": [
        "elephant", "giraffe", "kangaroo", "dolphin", "chimpanzee", "octopus",
        "penguin", "rhinoceros", "hippopotamus", "cheetah", "zebra", "tiger",
        "bear", "wolf", "fox", "owl", "eagle", "crocodile", "snake", "spider",
        "butterfly", "hummingbird", "panda", "koala", "lion", "whale"
    ],
    "food": [
        "pizza", "hamburger", "sushi", "spaghetti", "chocolate", "tacos",
        "burrito", "salad", "sandwich", "pancakes", "waffles", "ice cream",
        "cake", "cookies", "smoothie", "udon", "ramen", "curry", "dumplings",
        "lasagna", "omelette", "bread", "cheese", "yogurt", "soup"
    ],
    "countries": [
        "australia", "india", "united states", "canada", "mexico", "brazil", 
        "france", "germany", "italy", "spain", "china", "japan", "south africa", 
        "greece", "ireland", "new zealand", "peru", "chile", "sweden", "norway",
         "finland", "portugal", "argentina", "united kingdom", "egypt", "russia", 
    ]
}

# Topic descriptions
TOPIC_DESCRIPTIONS = {
    "movies": "Lights, camera, action! Guess the biggest blockbusters and classic films.",
    "books": "Open a new chapter! Can you guess these famous titles from literature?",
    "sports": "Game on! Test your knowledge of popular sports and athletic events.",
    "technology": "Future is now! Guess terms from the world of gadgets and innovation.",
    "history": "Journey through time! From ancient wonders to modern milestones.",
    "animals": "Wild encounters! Guess various creatures from across the globe.",
    "food": "Delicious delights! Can you guess these popular dishes and ingredients?",
    "countries": "Explore the world! Name these nations from every continent."
}

# Art for the hangman stages
HANGMAN_PICS = [
    # 0 wrong guesses
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    # 1 wrong guess
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    # 2 wrong guesses
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    # 3 wrong guesses
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    # 4 wrong guesses
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    # 5 wrong guesses
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    # 6 wrong guesses
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """,
    # 7 wrong guesses
    """
       -----
       |   |
      _O_  |
      /|\\  |
      / \\  |
           |
    ---------
    """,
    # 8 wrong guesses
    """
       -----
       |   |
      _X_  |
     _/|\\_ |
      / \\  |
           |
    ---------
    """
]

# --- Game Functions ---

def choose_topic():
    """Allows the user to select a topic from the available categories, displaying descriptions."""
    print("\n--- Select a Topic ---")
    print("Choose a category to test your knowledge!")
    for topic, desc in TOPIC_DESCRIPTIONS.items():
        print(f"- {topic.capitalize()}: {desc}")

    while True:
        choice = input("\nEnter your topic choice: ").lower()
        if choice in TOPICS:
            print(f"\nYou've chosen '{choice.capitalize()}'. Good luck!")
            return choice
        else:
            print("Invalid choice! Please pick a valid topic from the list.")

def choose_word(topic):
    """Selects a random word from the chosen topic's word bank."""
    return random.choice(TOPICS[topic])

def display_word(word, guessed_letters):
    """
    Returns a string representation of the word, showing guessed letters
    and underscores for unguessed letters. Handles spaces.
    """
    return " ".join(letter if letter in guessed_letters or letter == " " else "_" for letter in word)

def get_hint(secret_word, guessed_letters, hint_used):
    """
    Provides one random unguessed letter as a hint.
    Returns the hint letter or None if no hint is available or already used.
    """
    if hint_used:
        print("\nYou've already used your hint for this game!")
        return None

    unguessed_letters = [letter for letter in secret_word if letter.isalpha() and letter not in guessed_letters]

    if unguessed_letters:
        hint_letter = random.choice(unguessed_letters)
        print(f"\n--- HINT: The word contains the letter '{hint_letter.upper()}' ---")
        return hint_letter
    else:
        print("No more letters to hint! You've almost guessed them all.")
        return None

def word_guessing_game():
    """Main function to run the word guessing game."""
    print("--- Welcome to the Word Guessing Game! ---")
    print("Guess the secret word one letter at a time.")

    while True:
        topic = choose_topic()
        secret_word = choose_word(topic)
        guessed_letters = set()

        # Set the maximum wrong guesses directly to 8
        MAX_WRONG_GUESSES = 8 

        wrong_guesses_count = 0
        hint_used = False # Flag to track if the hint has been used

        print("\n--- Game Start! ---")
        print(f"Your word has {len(secret_word.replace(' ', ''))} letters (excluding spaces).")
        print(f"You have a maximum of {MAX_WRONG_GUESSES} wrong guesses.")

        # Initial display
        print(HANGMAN_PICS[wrong_guesses_count])
        print(f"Word: {display_word(secret_word, guessed_letters)}")

        # Display only incorrect guessed letters
        incorrect_guesses = [l for l in guessed_letters if l not in secret_word and l.isalpha()]
        print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses))}")

        print(f"Wrong guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses_count}")
        print("Type 'hint' for a clue (once per game).")

        while wrong_guesses_count < MAX_WRONG_GUESSES:
            guess = input("\nEnter a letter or 'hint': ").lower()

            if guess == "hint":
                if not hint_used:
                    hint_letter = get_hint(secret_word, guessed_letters, hint_used)
                    if hint_letter: # Only mark hint as used if a letter was actually provided
                        guessed_letters.add(hint_letter)
                        hint_used = True
                # No 'continue' here, as the display needs to update after hint
            elif len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please enter a single letter or 'hint'.")
                continue # Ask for input again if invalid

            elif guess in guessed_letters:
                print(f"You've already guessed '{guess}'. Try a different letter or ask for a 'hint'!")
                continue # Ask for input again if already guessed

            else: # Process the actual letter guess
                guessed_letters.add(guess)

                if guess in secret_word:
                    print("Good guess!")
                else:
                    print("Wrong guess!")
                    wrong_guesses_count += 1

            # --- Update game display after every action (guess or hint) ---
            print(HANGMAN_PICS[wrong_guesses_count])
            print(f"Word: {display_word(secret_word, guessed_letters)}")

            # Display only incorrect guessed letters
            incorrect_guesses = [l for l in guessed_letters if l not in secret_word and l.isalpha()]
            print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses))}")

            print(f"Wrong guesses remaining: {MAX_WRONG_GUESSES - wrong_guesses_count}")
            if not hint_used:
                print("Type 'hint' for a clue (once per game).") # Remind hint is available

            # Check for win condition after updating display
            if all(letter in guessed_letters or letter == " " for letter in secret_word):
                print("\n" + HANGMAN_PICS[wrong_guesses_count]) # Display final hangman state
                print(f"The word was: '{secret_word.upper()}'")
                print("\n--- CONGRATULATIONS! You've guessed the word correctly! YOU WIN! ---")
                break # Exit the inner game loop

        else: # This 'else' block executes if the while loop completes without a 'break' (i.e., ran out of attempts)
            print("\n" + HANGMAN_PICS[MAX_WRONG_GUESSES]) # Display full hangman
            print(f"\n--- GAME OVER! The secret word was '{secret_word.upper()}'. Better luck next time! ---")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! See you next time.")
            break # Exit the outer game loop

# Run the game
if __name__ == "__main__":
    word_guessing_game()