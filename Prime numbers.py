"""
This program is created to determine
if any integer is a prime or not.
User need to enter the number into field and
the program will identify the number as prime or not.
If the number is prime, the progrqm print "True".
If the number is not prime, the program print "False".
For undestanding of principes of determination
print "help".
"""

print(__doc__)

# Creating the function to determine the prime numbers
def is_prime(checking_number):
    """
This function determines prime numbers by enumeration of integers
"""
    divider = 2
    chopper = 0
    while (divider**2) <= checking_number and chopper != 1:
        if checking_number % divider == 0:
            chopper += 1
        else:
            divider += 1
    if chopper == 1:
        print('\nFalse')
    else:
        print('\nTrue')

# The function to modify entering user's data
def to_int(mod_number):
    while not type(mod_number) is int:
        try:
           mod_number = int(mod_number)
           if mod_number <= 1:
               print('\nPlease, enter the integer greater than 1.')
               mod_number = input('\nEnter the number: ')
        except ValueError:
            if mod_number == 'help':
                print(is_prime.__doc__)
                mod_number = input('\nEnter the number: ')
            else:
                print('\nPlease, enter the integer greater than 1.')
                mod_number = input('\nEnter the number: ')
    return mod_number
 
from variator import variator 


# Creation the body of this program
number = input('\nEnter the number: ')
number = to_int(number)
is_prime(number)

# Creation the cycles to repeat this program
repeater_set = variator('y') | variator('yes')
no_repeater_set = variator('n') | variator('no')
other_answers_set = repeater_set | no_repeater_set
repeater = input('''\nYou want to check another integer as prime?
If you want to check enter Y/y(Yes/yes).
If you want to exit enter N/n(No/no): ''')

while not repeater in other_answers_set:
    print("\Sorry, your answer cann't be understand. Please, enter your answer again!")
    repeater = input('''\nYou want to check another integer as prime?
If you want to check enter Y/y(Yes/yes).
If you want to exit enter N/n(No/no): ''')

while repeater in repeater_set:
    number = input('\nEnter the number: ')
    number = to_int(number)
    is_prime(number)
    repeater = input('''\nYou want to check another integer as prime?
If you want to check enter Y/y(Yes/yes).
If you want to exit enter N/n(No/no): ''')
    while not repeater in other_answers_set:
        print("\Sorry, your answer cann't be understand. Please, enter your answer again!")
        repeater = input('''\nYou want to check another integer as prime?
If you want to check enter Y/y(Yes/yes).
If you want to exit enter N/n(No/no): ''')
else:
    print('OK')