import random

##Functions
def hangmanpics():
    if lives==7:
        print('''
         _____
        |     |
              |
              |
              |
             _|_''')
    elif lives==6:
        print('''
         _____
        |     |
        O     |
              |
              |
             _|_''')

    elif lives==5:
        print('''
         _____
        |     |
        O     |
        |     |
              |
             _|_''')
    elif lives==4:
        print('''
         _____
        |     |
        O     |
        |     |
        |     |
             _|_''')

    elif lives==3:
        print('''
         _____
        |     |
        O     |
       /|     |
        |     |
             _|_''')
    elif lives==2:
        print('''
         _____
        |     |
        O     |
       /|\    |
        |     |
             _|_''')

    elif lives==1:
        print('''
         _____
        |     |
        O     |
       /|\    |
        |     |
       /     _|_''')

    elif lives==0:
        print('''
         _____
        |     |
        O     |
       /|\    |
        |     |
       / \   _|_''')
    
def wordpicker(w,c):
    creatures_list = ['unicorn', 'ghosts', 'dragon', 'vampire', 'zombie', 'goblin']
    snacks_list = ['Doritos chips', 'Goldfish crackers', 'Cheese balls', 'Onion Rings', 'Trail Mix']
    classics_list = ['A Space Odyssey', 'The Avengers', 'The Princess Bride', 'The Empire Strikes Back', 'Forrest Gump']
    random_list = creatures_list + snacks_list + classics_list
    c=''
    while (c==''):
        player_choice = str(input('Pick your category: ').upper())
        if player_choice == 'C':
            player_choice=creatures_list
            c+= 'Creatures'
        elif player_choice == 'S':
            player_choice=snacks_list
            c+= 'Snacks'
        elif player_choice == 'T':
            player_choice=classics_list
            c+= 'Classics'
        elif player_choice == 'R':
            player_choice=random_list
            c+= 'Random'
        else:
            print('Invalid category choice')
    w = random.choice(player_choice)
    return (w.lower(),c)
w=''
c=''

##[Game intro and Rules]
print('''[WELCOME to PYMAN !]
A game of Hangman in Python with the following rules:
-In order to win, you must guess the randomly generated word
within 7 failed attempts.
-The ways you can guess are either letter by letter or if you are
confident enough, try to guess the whole word!
-The categories of the words get more difficult with more words
With that said, have fun !
''')

##All code is nested in play variable for a redo button- ahh unfortunately makes it look much messier haha
play='YES'
while play == 'YES' or play == 'Y':
    guessed=False
    ##[Category choosing]
    print('''To begin, please pick a category of your choosing and preference of difficulty.
[EASY] Creatures(C)
[DIFFICULT] Snacks (S)
[HARD] Classic Titles (T)
[ALL] Random (R)
''')
    ##[Variables and extra text]
    word,category= wordpicker(w,c);
    print('The word has been generated from the',category,'category.')
    print('There are',len(word),'letters in the word.'+ '\nGood Luck guessing!')
    alphabet= (' abcdefghijklmnopqrstuvwxyz')
    lives = 7
    tries=0
    letters_guessed = ''
    guessed = False
    
    while guessed ==False:
        hangmanpics();
        print('\nLives left:',lives)
        player_guess= str(input('\nPlease enter your guess: ')).lower();
        letMissing = len(word)

    ##[Checking Input and Displaying Letters Guessed]
        
        if len(player_guess)==len(word) and player_guess in word: #If player guessed whole word
            tries+=1
            letters_guessed+=player_guess
            
        elif len(player_guess)==1 and player_guess in letters_guessed: #If player guesses same letter again
            print('You have already guessed '+player_guess+'.\n')
            
        elif len(player_guess)==1 and player_guess in alphabet: #If player enters one valid letter
            letters_guessed+=player_guess+' '
            tries+=1
            if player_guess in word:
                print('\nYou guessed correctly !\n')
            elif player_guess not in word:
                print('\nSorry, not in the word !\n')
                lives-=1
        
        else:
            print('Invalid input, please try again')
            
    ##[Displaying Word]
        for letter in word:
            if letter in letters_guessed:
                print(letter,end=' ')
                letMissing-=1
            else:
                print('_',end=' ')
        print('\t\tGuessed: '+letters_guessed)
            
    ##[Checking if full word is guessed or no more lives]
        if letMissing==0:
            print()
            for letter in ' ☆ ☆ CONGRATULATIONS! ☆ ☆ ':
                print(letter,end=' ')
            if tries==1:
                print('\nYou win and got it in',tries,'try!')
                guessed = True
            else:
                print('\nYou win and got it in',tries,'tries!')
                guessed = True
            
        elif lives==0:
            hangmanpics()
            print('Sorry, no more attempts left!')
            print('The word was',word,'!')
            for letter in 'GAME OVER':
                print(letter,end=' ')
            print()
            guessed = True
    ##[Redo Button]
    print()
    play= str(input('Would you like to play again?[YES/Y]: ').upper())
