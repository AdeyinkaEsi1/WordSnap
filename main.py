dictionary = {
    'lion': 'name of an animal',
    'articulate': 'well said/put',
    'lawyer': 'an individual that prosecutes or defends one in court'
}

try:
    user_input = input('word: ')
    if user_input in dictionary: print(dictionary[user_input])
    else: print('invalid')
except Exception as e: print(f'error: {e}')
    


