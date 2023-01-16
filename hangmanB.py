import os
import random
import time
import sys

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

# Initializing all the conditiosn for the game
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    
    limit = 5
    guess = imput("This is the Hangman word: " + display + "Enter your guess: \n")
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input! try a letter, please! \n")
        hangman()
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__   \n")
            print("Wrong guess!" + str(limit - count))
        elif count == 2:
            time.sleep(1)
            print("   _____\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__   \n")
            print"Wrong guess!" + str(limit - count) + "remaining guesses")
        elif count == 3:
            time.sleep(1)
            print("   _____\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__   \n")
            print"Wrong guess!" + str(limit - count) + "remaining guesses")
        elif count == 4:
            time.sleep(1)
            print("   _____\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O  \n"
                  "  |    /|\ \n"
                  "  |     \n"
                  "__|__   \n")
            print"Wrong guess!" + str(limit - count) + "remaining guesses")
        else:
            time.sleep(1)
            print("   _____\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O  \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__   \n")
            print("Wrong guess! You are henged!!!!\n")
            print("The word was: ", already_guesses, word)
            play_loop()
