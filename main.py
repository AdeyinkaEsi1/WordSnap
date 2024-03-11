import json
import random


def load_dictionary():
    """
    open a dictionary file and load the content into a dictionary"""
    try:
        with open('dictionary.json', 'r') as file:
            dictionary = json.load(file)
    except FileNotFoundError:
        dictionary =  {}
    return dictionary


def save_dictionary(dictionary):
    """
    save the dictionary to a file"""
    with open('dictionary.json', 'w') as file:
        json.dump(dictionary, file)


def print_all_words(dictionary):
    """
    print all the words in the dictionary"""
    for word in dictionary:
        print(word)


def print_random_word(dictionary):
    """
    print a random word from the dictionary"""
    if dictionary:
        random_word = random.choice(list(dictionary.keys()))
        print(f'{random_word}: {dictionary[random_word]}')
    else:
        print(f'{random_word} not found')


def add_new_word(dictionary):
    """
    add a new word to the dictionary"""
    new_word = input('Enter the new word: ')
    meaning = input(f'Enter the meaning of "{new_word}": ')
    dictionary[new_word.lower()] = meaning
    print (f'{new_word} added to dictionary')



def print_history(history):
    """
    print the history of user inputs"""
    for history_item in history:
        print(history_item)


def main():
    """
    main function to run the program"""
    dictionary = load_dictionary()
    user_input_history = []

    while True:
        user_input = input('Word (type "exit" to quit, "add" to add a new word): ').lower()

        if user_input == 'exit':
            save_dictionary(dictionary)
            print('Thank you for using wordsnap. See you soon')
            break
        elif user_input == 'all':
            print_all_words(dictionary)
        elif user_input == 'random':
            print_random_word(dictionary)
        elif user_input == 'add':
            add_new_word(dictionary)
        elif user_input == 'history':
            print_history(user_input_history)
        elif dictionary is not None and user_input in dictionary:
            print(f'The meaning of "{user_input}" is: {dictionary[user_input]}')
        else:
            print(f'Sorry, "{user_input}" not found in the dictionary. Please try another word.')

        user_input_history.append(user_input)

if __name__ == "__main__":
    main()

# =============================================

