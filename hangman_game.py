import random # Get word
import os # Clear screen


HANGMAN_STATUS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


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


def normalize(word):
    # List of accent marks
    replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
    # With the parameters of replacements
    for a, b in replacements:
        # If there is an letter with accent mark, replace it
        word_normalized = word.replace(a, b).replace(a.upper(), b.upper())
    # Return the string without accent marks
    return word_normalized


# This function will give all letters of the word, with all index of each word
    # Example:
        # guitarra = 'g': [0], 'u': [1], 'i': [2], 't': [3], 'a': [4, 7], 'r': [5, 6]
def dict_word(word):
    word_dict = {} # Create dict
    # For index - letters in word
    for idx, letter in enumerate(word):
        # If key letter 'not' in dict, add it in with a new index as 'value'
        if not word_dict.get(letter):
            word_dict[letter] = []
        # If key letter in dict, append his index as 'value'
        word_dict[letter].append(idx)
    # Return the dictionary
    return word_dict


def run():
    list_of_words = read_data()
    # Pick a random word from data
    raw_word = random.choice(list_of_words)
    # Normalize the word with the function 'normalize'
    word = normalize(raw_word)
    # Get the dict of the word
    word_dict = dict_word(word)

    print(word)
    print(len(word))
    print(word_dict)
    print(HANGMAN_PICS[0])


if __name__ == '__main__':
    run()
