import random

# Define a list of the top 10 Michael Jackson songs.
mj_songs = [
    "Billie Jean",
    "Thriller",
    "Beat It",
    "Smooth Criminal",
    "Black or White",
    "Bad",
    "The Way You Make Me Feel",
    "Don't Stop 'Til You Get Enough",
    "Man in the Mirror",
    "Rock with You"
]
score = 0

def play_game():
    global score
    print("Welcome to the Michael Jackson Song Guessing Game!")

    while True:
        # Choose a random song from the list.
        random_song = random.choice(mj_songs)

        print("\nGuess the Michael Jackson song:")
        print("Clue: It's one of MJ's top 10 hits.")

        guess = input("Your guess: ").strip()

        if guess.lower() == random_song.lower():
            score += 1
            print(f"Correct! Your score is now {score}.")
        else:
            print(f"Sorry, the correct answer was '{random_song}'. Your final score is {score}.")
            break

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print(f"Thanks for playing the Michael Jackson Song Guessing Game! Your final score is {score}.")
            break
