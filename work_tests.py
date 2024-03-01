def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a = 0
    b = 1
    while a < n:
        # print(a, end=' ')
        
        a, b = b, a+b
    # print('')

fib(2000)
"""
a = current val of b
b = previous val of a + b
"""
# print('\n')
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
    # print(f'index {str(index)} in supps is {item}')


import random
messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']
# print(messages[random.randint(0, len(messages) - 1)])
# random.shuffle(messages)
# print(messages)
name = 'OLAYINKA'
lv = '♡'
for i in name:
    i += lv
    # print(i)
    # print(f'♡ ♡ ♡ {i} ♡ ♡ ♡')


# import time, sys
# indent = 0
# indentIncreasing = True
# try:
#     while True:
#         for i in name:
#             print(' ' * indent, end='')
#             print(f'♡ ♡ ♡ {i} ♡ ♡ ♡')
#             time.sleep(0.2)
#             if indentIncreasing:
#                 indent += 1
#                 if indent == 20:
#                     indentIncreasing = False
#             else:
#                 indent = indent - 1
#             if indent == 0:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()
    



# def streaks():
#     choice = []
#     ch = []
#     nostrH = 0
#     nostrT = 0
#     tot_strH = 0
#     tot_strT = 0
#     strlen = 6
#     coin = ['H', 'T']
#     for i in range(100):
#         i = random.randint(0, 1)
#         if i == 0:
#             ch = coin[0]
#             choice.append(ch)
#             # print(choice)
#         else:
#             ch = coin[1]
#             choice.append(ch)
#             # print(choice)
#     # print(choice)
#     totH = 0
#     totT = 0
#     for i in choice:
#         if i == 'H':
#             # totH +=1
#             if nostrH < 6:
#                 nostrH +=1
#                 if nostrH == 6:
#                         tot_strH += 1
#             else: nostrH = 1
#         else:
#             # totT += 1
#             if nostrT < 6:
#                 nostrT +=1
#                 if nostrT == 6:
#                         tot_strT += 1
#             else: nostrT = 1
#     print(f'TOTAL OF streaks of H === {tot_strH}')
#     print(f'TOTAL OF streaks of T === {tot_strT}')

    



import random
import pprint

def generate_coin_flip_sequence(length):
    return ['heads' if random.randint(0, 1) == 0 else 'tails' for _ in range(length)]

def has_streak(sequence, streak_length):
    for i in range(len(sequence) - streak_length + 1):
        if all(sequence[i + j] == sequence[i] for j in range(streak_length)):
            return True
    return False

numberOfStreaks = 0
totalExperiments = 10000
streakLength = 6

for experimentNumber in range(totalExperiments):
    coinFlips = generate_coin_flip_sequence(100)
    if has_streak(coinFlips, streakLength):
        numberOfStreaks += 1

# pprint.pprint('Chance of streak: %s%%' % (numberOfStreaks / totalExperiments * 100))



print("""
                hi senior man i hope you are doing great
        """)

joe = '''joe'''





