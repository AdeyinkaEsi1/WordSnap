import json
import random


def load_dictionary():
    try:
        with open('dictionary.json', 'r') as file:
            dictionary = json.load(file)
    except FileNotFoundError:
        return {}


def save_dictionary():
    with open('dictionary', 'w') as file:
        json.dump(dictionary)


def print_all_words():
    for word in dictionary:
        print(word)

def print_random_words():
    if dictionary:
        random_word = random.choice(list(dictionary.keys()))
        print(f'{random_word}: {dictionary[random_word]}')
    else:
        print(f'{random_word} not found')
    


# =============================================
try:
    with open('dictionary.json', 'r') as file:
        dictionary = json.load(file)
except FileNotFoundError:
     dictionary = {}
user_input_history = []


while True:
        user_input = input('word (type "exit" to quit, add to add new word): ').lower()
        if user_input.lower() == 'exit':
            with open('dictionary.json', 'w') as file:
                json.dump(dictionary, file)
            print('Thank you for using wordsnap. See you soon')
            break
        elif user_input == 'all':
            for word, meaning in dictionary.items():
                print(f'{word}')
        elif user_input == 'random':
             random_word = random.choice(list(dictionary.keys()))
             random_meaning = dictionary[random_word]
             print(f' {random_word}: {random_meaning}')
        elif user_input == 'add':
             new_word = input('enter the new word: ')
             meaning = input(f'enter the meaning of {new_word}:  ')
             dictionary[new_word.lower()] = meaning
             print(f'{new_word} added to the dictionary')
        elif user_input == 'history':
            print(f'---INPUT HISTORY---')
            for history_item in user_input_history:
                print(history_item)
        elif user_input in dictionary: print(f'The meaning of "{user_input}" is: {dictionary[user_input]}')
        else: print(f'Sorry, "{user_input}" not found in the dictionary. Please try another word.')

        user_input_history.append(user_input)  

    

# ===============

# import json
# import random

# def load_dictionary():
#     try:
#         with open('dictionary.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}

# def save_dictionary(dictionary):
#     with open('dictionary.json', 'w') as file:
#         json.dump(dictionary, file)

# def print_all_words(dictionary):
#     for word in dictionary:
#         print(word)

# def print_random_word(dictionary):
#     if not dictionary:
#         print('Dictionary is empty.')
#         return
#     random_word = random.choice(list(dictionary.keys()))
#     print(f'{random_word}: {dictionary[random_word]}')

# def add_new_word(dictionary):
#     new_word = input('Enter the new word: ')
#     meaning = input(f'Enter the meaning of "{new_word}": ')
#     dictionary[new_word.lower()] = meaning
#     print(f'"{new_word}" added to the dictionary')

# def print_history(history):
#     for history_item in history:
#         print(history_item)

# def main():
#     dictionary = load_dictionary()
#     user_input_history = []

#     while True:
#         user_input = input('Word (type "exit" to quit, "add" to add a new word): ').lower()

#         if user_input == 'exit':
#             save_dictionary(dictionary)
#             print('Thank you for using wordsnap. See you soon')
#             break
#         elif user_input == 'all':
#             print_all_words(dictionary)
#         elif user_input == 'random':
#             print_random_word(dictionary)
#         elif user_input == 'add':
#             add_new_word(dictionary)
#         elif user_input == 'history':
#             print_history(user_input_history)
#         elif user_input in dictionary:
#             print(f'The meaning of "{user_input}" is: {dictionary[user_input]}')
#         else:
#             print(f'Sorry, "{user_input}" not found in the dictionary. Please try another word.')

#         user_input_history.append(user_input)

# if __name__ == "__main__":
#     main()
