import random

# Define a dictionary of the top 10 Michael Jackson songs.
mj_songs = {
    "Billie Jean": "One of Michael Jackson's most iconic hits.",
    "Thriller": "The title track from his best-selling album.",
    "Beat It": "A classic song with an iconic guitar solo.",
    "Smooth Criminal": "Known for its catchy chorus and Moonwalk dance.",
    "Black or White": "Addresses themes of unity and racial harmony.",
    "Bad": "Title track from the 'Bad' album.",
    "The Way You Make Me Feel": "An upbeat and catchy love song.",
    "Don't Stop 'Til You Get Enough": "Disco-funk track from 'Off the Wall'.",
    "Man in the Mirror": "Encourages personal change and reflection.",
    "Rock with You": "A soulful, funky love song."
}

# Create a list of song titles for random selection.
song_titles = list(mj_songs.keys())

# Set the number of tries allowed.
max_tries = 3

# Initialize the scoreboard.
score = 0

def play_game():
    global score
    print("Welcome to the Michael Jackson Song Guessing Game!")

    while True:
        # Choose a random song from the list.
        random_song = random.choice(song_titles)
        song_description = mj_songs[random_song]

        print("\nGuess the Michael Jackson song:")
        print(f"Clue: {song_description}")

        tries = 0
        while tries < max_tries:
            guess = input("Your guess: ").strip()
            if guess == random_song:
                score += 1
                print(f"Correct! Your score is now {score}.")
                break
            else:
                tries += 1
                if tries < max_tries:
                    print(f"Sorry, that's incorrect. You have {max_tries - tries} tries left.")
                else:
                    print(f"Sorry, you're out of tries. The correct answer was '{random_song}'. Your final score is {score}.")
                    break

if __name__ == "__main__":
    while True:
        score = 0
        play_game()
        play_again = input("Play again? (yes/no): ").strip().lower()
        print("Play again? (yes/no): ")
        if play_again != "yes":
            print(f"Thanks for playing! Your final score is {score}.")
            break
