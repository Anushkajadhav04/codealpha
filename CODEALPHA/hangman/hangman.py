import random

words = ["python", "apple", "chair", "table", "house"]

def play_game():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6
    hint_used = False

    def display_word():
        return " ".join([letter if letter in guessed_letters else "_" for letter in word])

    print("\n🎮 Welcome to Hangman!")

    while wrong_guesses < max_attempts:
        print("\nWord:", display_word())
        print("Attempts left:", max_attempts - wrong_guesses)

        choice = input("Enter a letter or type 'hint': ").lower()

        # Hint feature
        if choice == "hint":
            if not hint_used:
                hint_letter = random.choice(word)
                print("💡 Hint: The word contains letter:", hint_letter)
                hint_used = True
            else:
                print("⚠️ Hint already used!")
            continue

        # Input validation
        if not choice.isalpha() or len(choice) != 1:
            print("⚠️ Enter a single valid letter!")
            continue

        if choice in guessed_letters:
            print("⚠️ Already guessed!")
            continue

        guessed_letters.append(choice)

        if choice in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            wrong_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You won! The word was:", word)
            return

    print("\n💀 You lost! The word was:", word)


# Replay feature
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break