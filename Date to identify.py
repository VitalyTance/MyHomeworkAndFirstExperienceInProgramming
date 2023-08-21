"""
This programm identify a real date built by day, month and year.
User need to enter in special fields the integer number and
program will identify if the date is real or not.
If date is real program print message "True".
Id date is not real program print message "False".
For additional information enter "help".
"""

print(__doc__)


# The creation of the function to determine real date
from datetime import datetime

import numpy

def identify_the_date(id_year, id_month, id_day):
    try:
        numpy.datetime64('{}-{}-{}'.format(id_year, id_month, id_day))
        print('True')
    except ValueError:
        print('False')

# The creation of the function to modify user data
def to_int_day(mod_day):
    """
You need to enter integer as the day you want to check.
For example: 23
"""
    while not type(mod_day) is int:
        try:
            mod_day = int(mod_day)
        except ValueError:
            if mod_day == 'help':
                print(to_int_day.__doc__)
                mod_day = input('Enter the day: ')
            else:
                print('Please, enter the integer.')
                mod_day = input('Enter the day: ')
    return mod_day

def to_int_month(mod_month):
    """
You need to enter integer as the month you want to check.
For example: 6
"""
    while not type(mod_month) is int:
        try:
            mod_month = int(mod_month)
        except ValueError:
            if mod_month == 'help':
                print(to_int_month.__doc__)
                mod_month = input('Enter the month: ')
            else:
                print('Please, enter the integer.')
                mod_month = input('Enter the month: ')
    return mod_month

def to_int_year(mod_year):
    """
You need to enter integer as the year you want to check.
For example: 1995
"""
    while not type(mod_year) is int:
        try:
            mod_year = int(mod_year)
        except ValueError:
            if mod_year == 'help':
                print(to_int_year.__doc__)
                mod_year = input('Enter the year: ')
            else:
                print('Please, enter the integer.')
                mod_year = input('Enter the year: ')
    return mod_year

    
# The creation of body of the program
day = input('Enter the day: ')
day = to_int_day(day)
month = input('Enter the month: ')
month = to_int_month(month)
year = input('Enter the year: ')
year = to_int_year(year)
identify_the_date(str(year), str(month), str(day))

# The creation of the cycles to repeat program
from variator import variator

repeater_set = variator('y') | variator('yes')
no_repeater_set = variator('n') | variator('no')
other_answers_set = repeater_set | no_repeater_set
repeater = input("Do you want to check another date?")

while not repeater in other_answers_set:
    print("Sorry, your answer cann't be understand")
    repeater = input("Do you want to check another date?")

while repeater in repeater_set:
    day = input('Enter the day: ')
    day = to_int_day(day)
    month = input('Enter the month: ')
    month = to_int_month(month)
    year = input('Enter the year: ')
    year = to_int_year(year)
    identify_the_date(str(year), str(month), str(day))
    repeater = input("Do you want to check another date?")
    while not repeater in other_answers_set:
        print("Sorry, your answer cann't be understand")
        repeater = input("Do you want to check another date?: ")
else:
    print('OK')
