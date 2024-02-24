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



print(int.__add__(4, 12))
print(str.__add__('hello', ' world'))

class Devs:
    comapny = 'Diarupt'

    @classmethod
    def get_stack(cls, stack, empname):
        empname = input('Enter employee name: ')
        print(f'The stack of {empname} of {Devs.comapny} is {stack}')



Devs.get_stack('Python', 'Josh')
