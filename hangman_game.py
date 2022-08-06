import random # Get word
import os # Clear screen

TOTAL_LIFES = 6
HANGMAN = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       
            by Fabricio Quintas
'''

MENU = '''
______________________________________________________________                       
|     BIENVENIDO AL JUEGO DEL AHORACADO o HANGMAN GAME        |
--------------------------------------------------------------
Para comenzar presiona (s) y luego (Enter)
Para salir presiona cualquier otra tecla
______________________________________________________________
'''

PICS = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

WIN_MESSAGE = '''
  /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$
 /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$ /$$__  $$|__  $$__/| $$_____/
| $$  \__/| $$  \ $$| $$$$| $$| $$  \ $$| $$  \__/   | $$   | $$      
| $$ /$$$$| $$$$$$$$| $$ $$ $$| $$$$$$$$|  $$$$$$    | $$   | $$$$$   
| $$|_  $$| $$__  $$| $$  $$$$| $$__  $$ \____  $$   | $$   | $$__/   
| $$  \ $$| $$  | $$| $$\  $$$| $$  | $$ /$$  \ $$   | $$   | $$      
|  $$$$$$/| $$  | $$| $$ \  $$| $$  | $$|  $$$$$$/   | $$   | $$$$$$$$
 \______/ |__/  |__/|__/  \__/|__/  |__/ \______/    |__/   |________/
'''

LOSE_MESSAGE = '''
 _______  ________  _______     ______   _____   ______   _________  ________  
|_   __ \|_   __  ||_   __ \   |_   _ `.|_   _|.' ____ \ |  _   _  ||_   __  | 
  | |__) | | |_ \_|  | |__) |    | | `. \ | |  | (___ \_||_/ | | \_|  | |_ \_| 
  |  ___/  |  _| _   |  __ /     | |  | | | |   _.____`.     | |      |  _| _  
 _| |_    _| |__/ | _| |  \ \_  _| |_.' /_| |_ | \____) |   _| |_    _| |__/ | 
|_____|  |________||____| |___||______.'|_____| \______.'  |_____|  |________| 
'''

ASK_CONTINUE = '''
Si quieres jugar otra partida, presiona 's' y luego (Enter)
      Para salir presiona cualquier otra tecla
'''


def read_data():
    try:
        # Open data.txt from this folder
        with open("./data.txt", "r", encoding="utf-8") as f:
            # Strip the lines of the data
            data = [line.strip() for line in f]
        # Put it in dictionary, with enumerate function
        # This will give to each line a number, and it will be his index
        data = {key: value for key, value in enumerate(data)}
        return data
    except:
        # If can't open it, print an error and quit
        print("Can't find the data named 'data.txt', please try again")
        quit()


def initGame(data):
    raw_word = random.choice(data).lower() # Pick a random word from data
    word = normalize(raw_word).upper() # Normalize the word with the function 'normalize'
    word_dict = dict_word(word) # Get the dict of the word
    hidden_word = ["_"] * len(word)
    # Return all variables
    return word, word_dict, hidden_word


def normalize(word): # Delete accent mark from a word
    # List of accent marks and his common letters
    a,b = 'áéíóúü','aeiouu'
    # Maketrans function to change this letters
    transcription = str.maketrans(a,b)
    # Make the translation
    word_normalize = word.translate(transcription)
    # Return the string without accent marks
    return word_normalize


# This function will give all letters of the word, with all index of each word
    # Example:
        # guitarra = 'g': [0], 'u': [1], 'i': [2], 't': [3], 'a': [4, 7], 'r': [5, 6]
def dict_word(word):
    word_dict = {} # Create dict
    # For index - letters in word
    for idx, letter in enumerate(word):
        # If key letter 'not' in dict, add it in with a new index as 'value'
        if not word_dict.get(letter.upper()):
            word_dict[letter.upper()] = []
        # If key letter in dict, append his index as 'value'
        word_dict[letter.upper()].append(idx)
    # Return the dictionary
    return word_dict


def updateScreen(hangman_state, first_run, word, won):
    current_lifes = TOTAL_LIFES - hangman_state # Check current lifes

    os.system("clear") # Clear Terminal
    print(HANGMAN) # Print HANGMAN logo

    # If hangman_state is 6, he lose
    if hangman_state == 6:
        print(LOSE_MESSAGE) # Print lose message
        print("La palabra era:", word) # Show hidden word
        print(ASK_CONTINUE) # Ask if want to continue
    # If first run is true show menu
    elif first_run == True:
        print(MENU) # Show menu
    else:
        # Remember how many lifes remaining
        print("Recuerda, tienes", current_lifes, "vidas, ten cuidado")
        print(PICS[hangman_state]) # Print current hangman status
    
    if won == True:
        os.system("clear") # Clear Terminal
        print(WIN_MESSAGE)
        print(ASK_CONTINUE)


def run():
    data = read_data()
    word, word_dict, hidden_word = initGame(data)

    hangman_state = 0 # First state of hangman
    first_run = True # First run
    won = False
    
    while True:
        updateScreen(hangman_state, first_run, word, won)
        # Change first run to false
        if first_run == True:
            first_run = False
        # Read the input
        user_input = input()
        # Check answer if he lose / win
        if hangman_state == 6 or won == True:
            if user_input.strip().upper() == 'S':
                hangman_state = 0 # Restart hangman state
                won = False # Reset won status
                word, word_dict, hidden_word = initGame(data) # Init the game again
            else:
                print("Gracias por jugar mi juego")
                quit()
        # os.system("clear") # Clear terminal
        # print(HANGMAN) # Print HANGMAN
        # user_input = input(MENU)
        
        # Check if the input is the letter 's' to continue, or any else to quit
        try:
            user_input = user_input.strip().upper()
            # If the user input is NOT 'S', quit game
            if user_input != "S":
                print("Gracias por probar mi juego")
                quit()
            # Start a cicle, when hangman reach 6 the user loss
            while hangman_state < 6 and won == False:
                # Update screen
                updateScreen(hangman_state, first_run, word, won)
                # Hidden Word have the len of the word as underscores or guessed letters
                for chars in hidden_word:
                    # Print them all 1 by 1
                    print(chars + " ", end="")
                print("\n")

                try:
                    letter = input("Ingresa una letra y presiona (Enter): ").strip().upper()
                    # Assert that is a letter, and is only one
                    assert letter.isalpha(), "¡Solo puedes ingresar letras!"
                    assert len(letter) == 1, "¡Solo UNA letra!"
                except AssertionError as e:
                    print(e)
                
                # If letter is in word dict, and not in the revealed one
                if letter in word_dict and letter not in hidden_word:
                    # Reveal it with all his index
                    for index in word_dict[letter]:
                        hidden_word[index] = letter
                # If already guessed, past to next state
                elif letter in hidden_word:
                    hangman_state += 1
                    already_guessed = True
                    print("¡Ya ingresaste esa letra! Pierdes una vida")
                # If not there, pass to the next state
                else:
                    hangman_state += 1
                    print("Esa letra no se encuentra en la palabra, pierdes una vida")

                if not "_" in hidden_word:
                    won = True


                # print(PICS[hangman_state])
                # won = True
                # print(PICS[6])
                
        except KeyboardInterrupt as f:
            print(f)
            quit()
        
    # print(word)
    # print(len(word))
    # print(word_dict)
    # print(HANGMAN)
    # print(PICS[0],"\n", PICS[6])
    # print(WIN_MESSAGE)
    # print(LOSE_MESSAGE)

if __name__ == '__main__':
    run()