# class Diarupt:
#     # def __init__(self, name, age, yoe):
#     name = 'josh'
#     age = 25
#     yoe = 2023,
#     level = 'B'

#     @classmethod
#     def output(cls, eff):
#         eff = cls.yoe // 10
#         print(f'the eff is {eff}')


# Diarupt.output()


# class MathOperations:
#     pi = 3.14159

#     @classmethod
#     def circle_area(cls, radius):
#         area = cls.pi * (radius ** 2)
#         print(f"The area of a circle with radius {radius} is: {area:.1f}")

#     @classmethod
#     def cylinder_volume(cls, radius, height):
#         volume = cls.pi * (radius ** 2) * height
#         print(f"The volume of a cylinder with radius {radius} and height {height} is: {volume:.2f}")

# # Use class methods to perform math operations
# MathOperations.circle_area(5)
# MathOperations.cylinder_volume(5, 10)



# print(int.__add__(4, 12))
# print(str.__add__('hello', ' world'))

# class Devs:
#     comapny = 'Diarupt'

#     @classmethod
#     def get_stack(cls, stack, empname):
#         empname = input('Enter employee name: ')
#         print(f'The stack of {empname} of {Devs.comapny} is {stack}')



# Devs.get_stack('Python', 'Josh')

alist = [
'Lists of animals',
'Lists of aquarium life',
'Lists of biologists by author abbreviation',
'Lists of cultivars']

# for i in alist:
    # print(f'* {i}')


# apples Alice dogs
# oranges Bob cats
# cherries Carol moose
# banana David goose

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
# ['Alice', 'Bob', 'Carol', 'David'],
# ['dogs', 'cats', 'moose', 'goose']]


# def printTable(tableData):
#     # Find the maximum width of each column
#     col_widths = [max(len(item) for item in col) for col in zip(*tableData)]

#     # Transpose the table for easy printing
#     transposed_table = [list(row) for row in zip(*tableData)]

#     # Print the table with right-justified columns
#     for row in transposed_table:
#         print(''.join(item.rjust(width) for item, width in zip(row, col_widths)))


# printTable(tableData)

# ff= 'p'
# print(ff.isdecimal())



import re


heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

# =======================================
# Special characters
# \	escape special characters
# .	matches any character
# ^	matches beginning of string
# $	matches end of string
# [5b-d]	matches any chars '5', 'b', 'c' or 'd'
# [^a-c6]	matches any char except 'a', 'b', 'c' or '6'
# R|S	matches either regex R or regex S
# ()	creates a capture group and indicates precedence
# Quantifiers===============================================
# *	0 or more (append ? for non-greedy)
# +	1 or more (append ? for non-greedy)
# ?	0 or 1 (append ? for non-greedy)
# {m}	exactly mm occurrences
# {m, n}	from m to n. m defaults to 0, n to infinity
# {m, n}?	from m to n, as few as possible
# Special sequences=========================================
# \A	start of string
# \b	matches empty string at word boundary (between \w and \W)
# \B	matches empty string not at word boundary
# \d	digit
# \D	non-digit
# \s	whitespace: [ \t\n\r\f\v]
# \S	non-whitespace
# \w	alphanumeric: [0-9a-zA-Z_]
# \W	non-alphanumeric
# \Z	end of string
# \g<id>	matches a previously defined group
# Special sequences================================================
# (?iLmsux)	matches empty string, sets re.X flags
# (?:...)	non-capturing version of regular parentheses
# (?P...)	matches whatever matched previously named group
# (?P=)	digit
# (?#...)	a comment; ignored
# (?=...)	lookahead assertion: matches without consuming
# (?!...)	negative lookahead assertion
# (?<=...)	lookbehind assertion: matches if preceded
# (?<!...)	negative lookbehind assertion
# (?(id)yes|no)	match 'yes' if group 'id' matched, else 'no'