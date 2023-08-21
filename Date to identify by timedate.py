"""
This programm identify a real date built by day, month and year.
User need to enter in special fields the integer number and
program will identify if the date is real or not.
If date is real program print message "True".
Id date is not real program print message "False".
"""

print(__doc__)


# The creation of another version of program to identify date
from datetime import datetime

def identify_the_date(id_year, id_month, id_day):
    try:
        datetime(id_year, id_month, id_day)
        print('\nTrue')
    except ValueError:
        print('\nFalse')

# The defence of entering data from user
def to_int(*element_of_the_year):
    mod_element_of_the_year = list(element_of_the_year)
    for i in range(0, 3, 1):
        while not type(mod_element_of_the_year[i]) is int:
            try:
                mod_element_of_the_year[i] = int(mod_element_of_the_year[i])
            except ValueError:
                if i == 2:
                    print('\nEnter the integer, please!')
                    mod_element_of_the_year[2] = input('\nEnter the day: ')
                elif i == 1:
                    print('\nEnter the integer, please!')
                    mod_element_of_the_year[i] = input('\nEnter the month: ')
                elif i == 0:
                    print('\nEnter the integer, please!')
                    mod_element_of_the_year[i] = input('\nEnter the year: ')
    return mod_element_of_the_year


# The body of the program
day = input('\nEnter the day: ')
date_list = to_int(0, 0, day)
day = date_list[2]
month = input('\nEnter the month: ')
date_list = to_int(0, month, day)
month = date_list[1]
year = input('\nEnter the year: ')
date_list = to_int(year, month, day)
year = date_list[0]
identify_the_date(year, month, day)

# The creation of body of the program
from variator import variator as vari
repeater_set = vari('y') | vari('yes')
no_repeater_set = vari('n') | vari('no')
other_answers_set = repeater_set | no_repeater_set
repeater = input('''\nDo you want to check another date?
If you want to check enter Y/y(Yes/yes)
If you want to exit enter N/n(No/no): ''')

while not repeater in other_answers_set:
    print("\nSorry, your answer cann't be understand. Enter your answer again")
    repeater = input('''\nDo you want to check another date?
If you want to check enter Y/y(Yes/yes)
If you want to exit enter N/n(No/no): ''')

while repeater in repeater_set:
    day = input('\nEnter the day: ')
    date_list = to_int(0, 0, day)
    day = date_list[2]
    month = input('\nEnter the month: ')
    date_list = to_int(0, month, day)
    month = date_list[1]
    year = input('\nEnter the year: ')
    date_list = to_int(year, month, day)
    year = date_list[0]
    identify_the_date(year, month, day)
    repeater = input('''\nDo you want to check another date?
If you want to check enter Y/y(Yes/yes)
If you want to exit enter N/n(No/no): ''')
    while not repeater in other_answers_set:
        print("\nSorry, your answer cann't be understand. Enter your answer again")
        repeater = input('''\nDo you want to check another date?
If you want to check enter Y/y(Yes/yes)
If you want to exit enter N/n(No/no): ''')
else:
    print('OK')
