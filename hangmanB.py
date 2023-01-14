import random
import time

# initial steps to invite in the game:

print("\nWelcome to Hangman!\n")
name = input("\nWhat is your name?\n")
print("Hello " + name + "! Good Luck!")
time.sleep(1)
print("Loading")
time.sleep(2)
print("The game is about to start!\n Let us play Hangman!")
time.sleep(3)



# Parameter we require to execute

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    words_list = ["march", "superb", "splendid", "spiderman",
    "deahtstroke", "chocolate", "heart", "happy", "toronto",
    "cairo", "warsaw", "paris", "chicago", "edmonton"]

    word = random.choice(words_list)
    print(word)


    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Wanna play again? (y/n)\n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Wanna play again? (y/n)\n")
    if play_game == "y" or play_game == "Y":
        main()
    elif play_game == "n" or play_game == "n":
        print("Bye! See You Later !")
        exit()
