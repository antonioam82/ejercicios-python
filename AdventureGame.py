import time
import os
from colorama import Fore, init, Style

init()

weapon = False

def clear_screen():
  try:
    os.system('cls')
  except:
    pass

def typer(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)

def play_again():
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == "y":
            start_game()
        elif play_again == "n":
            print("Thank you for playing! Goodbye. ")
            time.sleep(2)
            quit()
        else:
            print(Fore.RED+Style.Style.DIM+"Please enter a valid option ('y' or 'n'). "+Fore.RESET+Style.RESET_ALL)

def introScene():
  clear_screen()
  directions = ["left", "right", "forward"]
  typer(Fore.GREEN+"You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?\n"+Fore.RESET)
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      showShadowFigure()
    elif userInput == "right":
      showSkeletons()
    elif userInput == "forward":
      hauntedRoom()
    elif userInput == "backward":
      clear_screen()
      typer(Fore.GREEN+"You find that this door opens into a wall.\n"+Fore.RESET)
    else: 
      print(Fore.RED+Style.Style.DIM+"Please enter a valid option for the adventure game."+Fore.RESET+Style.RESET_ALL)

def showSkeletons():
  clear_screen()
  directions = ["backward", "forward"]
  global weapon
  typer(Fore.GREEN+"You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?\n"+Fore.RESET)
  userInput = ""
  while userInput not in directions:
    print("Options: left/backward/forward")
    userInput = input()
    if userInput == "left":
      clear_screen()
      typer(Fore.GREEN+"You find that this door opens into a wall. You open some of the drywall to discover a knife.\n"+Fore.RESET)
      weapon = True
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Please enter a valid option for the adventure game.")

def strangeCreature():
  clear_screen()
  actions = ["fight", "flee"]
  global weapon
  typer(Fore.GREEN+"A strange goul-like creature has appeared. You can either run or fight it. What would you like to do?\n"+Fore.RESET)
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      clear_screen()
      if weapon:
        typer(Fore.GREEN+"You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congrats! "+Fore.RESET)
      else:
        typer(Fore.GREEN+"The goul-like creature has killed you.\n"+Fore.RESET)
      play_again()
    elif userInput == "flee":
      showSkeletons()
    else:
      print("Please enter a valid option for the adventure game.")

def showShadowFigure():
  clear_screen()
  directions = ["right", "backward"]
  typer(Fore.GREEN+"You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?\n"+Fore.RESET)
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      clear_screen()
      typer(Fore.GREEN+"You find that this door opens into a wall.\n"+Fore.RESET)
      #...
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option for the adventure game.")

def cameraScene():
  clear_screen()
  directions = ["forward", "backward"]
  typer(Fore.GREEN+"You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?\n"+Fore.RESET)
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      clear_screen()
      typer(Fore.GREEN+"You made it! You've found an exit.\n"+Fore.RESET)
      play_again()
    elif userInput == "backward":
      showShadowFigure()
    else:
      print("Please enter a valid option for the adventure game.")

def hauntedRoom():
  clear_screen()
  directions = ["right", "left", "backward"]
  typer(Fore.GREEN+"You hear strange voices. You think you have awoken some of the dead. Where would you like to go?\n"+Fore.RESET)
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      clear_screen()
      typer(Fore.GREEN+"Multiple goul-like creatures start emerging as you enter the room. You are killed.\n"+Fore.RESET)
      play_again()
    elif userInput == "left":
      clear_screen()
      typer("You made it! You've found an exit.\n")
      play_again()
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option for the adventure game.")

def start_game():
  clear_screen()
  typer(Fore.GREEN+"Welcome to the Adventure Game! "+Fore.RESET)
  typer(Fore.GREEN+"As an avid traveler, you have decided to visit the Catacombs of Paris. "+Fore.RESET)
  typer(Fore.GREEN+"However, during your exploration, you find yourself lost. "+Fore.RESET)
  typer(Fore.GREEN+"You can choose to walk in multiple directions to find a way out.\n"+Fore.RESET)
  typer(Fore.GREEN+"Let's start with your name: "+Fore.RESET)
  name = input()
  print("Good luck, " +name+ ".")
  time.sleep(2)
  introScene()

start_game()

if __name__ == '__main__':
  start_game()
