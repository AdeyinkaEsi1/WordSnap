#  ===========  COLLATZ SEQUENCE  ============
# def collatz():
#     number = int(input(f'Enter a number: '))
#     while number > 1:
#         print(number)
#         if number % 2 == 0:
#             number = number // 2
#         else:
#             number = number * 3 + 1

#     print(number)

    
# collatz()


# ========FACTORIAL CALCULATION========


# number = int(input('no: '))

# if number > 0:
#     fac = 1
#     for i in range(1, number + 1):
#         fac *= i
#     print(fac)


# ==================
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Get user input
# number = int(input("Enter a non-negative integer: "))

# # Check if the input is non-negative
# if number < 0:
#     print("Please enter a non-negative integer.")
# else:
#     result = factorial(number)
#     print(f"The factorial of {number} is: {result}")




class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
print(dev_1.fullname())

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_2])

print(issubclass(Developer, Manager))

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
