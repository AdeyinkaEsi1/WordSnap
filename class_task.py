# model = {
#     'name': 'Emile',
#     'model_type': 'Predictive AI',
#     'desc': [
#         'introduces itself',
#         'takes name and club input from user and responds' -- instance method
#         'returns list of matches available'
#         'takes input and predict game outcome'
#     ]
# }

import random

class AI:
    name = 'Emile'
    model_type = 'Predictive AI'
    matches = {
        '1': 'celtic v rangers',
        '2': 'soton v luton',
        '3': 'spurs v palace'
    }

    def __init__(self, username, club):
        self.username = username
        self.club = club

    @classmethod
    def greetings(cls):
        print(f'Hi i am {AI.name}, a {AI.model_type}. I specialize in predicting the outcome of football matches')

    def know_user(self):
        print('can i know your name and club you support?')
        if self.username and self.club:
            print(f'Nice to meet you {self.username}. You support a great club in {self.club}')

    @classmethod
    def list_of_matches(cls):
        print('These are the available matches you can select from. choose a number to get a prediction')
        for key, value in AI.matches.items():
            print(f'{key}: {value}')


    def predict():
        try:
            selected_match_number = int(input('choose number: '))
        except ValueError:
            print('Invalid input. Please enter 1, 2 or 3.')
            return

        if str(selected_match_number) in AI.matches:
            teams = AI.matches[str(selected_match_number)].split('v')
            choice = random.choice(teams)
            print(f'I will go for {choice}')
        else:
            pass
        




AI.greetings()
ai = AI( username=input('name: '), club=input('club: '))
ai.know_user()
AI.list_of_matches()
AI.predict()



#  if selected_match_number == 1:
#             choice = random.choice(['rangers', 'celtic'])
#             print(f'i will go for {choice}')
#         elif selected_match_number == 2:
#             choice = random.choice(['soton', 'luton'])
#             print(f'i will go for {choice}')
#         elif selected_match_number == 3:
#             choice = random.choice(['everton', 'palace'])
#             print(f'i will go for {choice}')
#         else: print('wrong input')