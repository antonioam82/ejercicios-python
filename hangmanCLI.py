import os
import random
import time
import re
import sys

print("\nWelcome to Hangman!\n")
name = input("\nWhat is your name?\n")
print("Hello " + name + "! Good Luck!")
time.sleep(1)
print("GET READY..")
time.sleep(2)
print("The game is about to start!\nLet us play Hangman!\n")
time.sleep(1)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    words_list = ["march", "superb", "splendid", "spiderman",
    "deahtstroke", "chocolate", "heart", "happy", "toronto",
    "cairo", "warsaw", "paris", "chicago", "edmonton","dog","school",
    "people","catwoman","stratosphere","rocket","stradivarius"]

    word = random.choice(words_list)
    print(word)


    length = len(word)
    count = 0
    display = ['_'] * length
    already_guessed = []
    #play_game = ""

    hangman()

def add_letter(l):
    global display
    #global already_guessed
    global word
    for c in re.finditer(l, word, re.IGNORECASE):
        display[c.start():c.end()] = list(c.group())
    for c in re.finditer(l, word, re.IGNORECASE):
        display[c.start()] = c.group()
    print("".join(display))

def play_loop():
    #global play_game
    play_game = input("Wanna play again? (y/n)\n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Wanna play again? (y/n)\n")
    if play_game == "y" or play_game == "Y":
        main()
    elif play_game == "n" or play_game == "n":
        print("Bye! See You Later !")
        exit()
        
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    
    limit = 5
    guess = input("This is the Hangman word: " + ("".join(display)) + " Enter your guess: \n")
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input! try a letter, please! \n")
        hangman()
    elif guess in already_guessed:
        print(f"Letter '{guess}' is already guessed. Try another letter.\n")
    elif guess in word:
        already_guessed.append(guess)
        add_letter(guess)
    else:
        count += 1
        time.sleep(1)
        if count == 1:
            print("   _____\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__   \n")
            print("Wrong guess!: " + str(limit - count) +" remaining guesses")
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
            print("Wrong guess!: " + str(limit - count) +" remaining guesses")
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
            print("Wrong guess!: " + str(limit - count) +" remaining guesses")
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
            print("Wrong guess!: " + str(limit - count) +" remaining guesses")
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
            print("Wrong guess! You are hanged!!!!\n")
            print("The word was: ", word)
            play_loop()

    if ("".join(display)) == word:
        print("Congrats!!! You are alive!")
        play_loop()
    elif count != limit:
        hangman()

main()

