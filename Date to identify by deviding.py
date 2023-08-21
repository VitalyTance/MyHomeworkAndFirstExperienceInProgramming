"""
This programm identify a real date built by day, month and year.
User need to enter in special fields the integer number and
program will identify if the date is real or not.
If date is real program print message "True".
Id date is not real program print message "False".
For additional information enter "help".
"""

print(__doc__)


# The creation the function to identify the date by deviding
def identify_the_date(id_year, id_month, id_day):
    """
You need to fill the special field with integers.
For example: in field "Enter the day" you can input 29
             in field "Enter the month" - 3
             in field "Enter the year" - 2023
             in result you will get the line "2023-3-29"
The data determined by realisation condition checking algorithm.
"""
    high_months = (1, 3, 5, 7,
                   8, 10, 12)
    low_months = (4, 6, 9, 11)
    february = 2
    if 0 < id_day <= 31 and id_month in high_months:
        print('\nTrue')
    elif 0 < id_day < 31 and id_month in low_months:
        print('\nTrue')
    elif 0 < id_day < 29 and id_month == february:
        print('\nTrue')
    elif 0 < id_day <=29 and id_month == february and id_year%4 == 0:
        print('\nTrue')
    else:
        print('\nFalse')

# The defence of entering data from user
def to_int(*element_of_the_year):
    mod_element_of_the_year = list(element_of_the_year)
    for i in range(0, len(mod_element_of_the_year), 1):
        while not type(mod_element_of_the_year[i]) is int:
            try:
                mod_element_of_the_year[i] = int(mod_element_of_the_year[i])
            except ValueError:
                if mod_element_of_the_year[2] == 'help':
                    print(identify_the_date.__doc__)
                    mod_element_of_the_year[2] = input('\nEnter the day: ')
                elif i == 2:
                    print('\nEnter the integer, please!')
                    mod_element_of_the_year[2] = input('\nEnter the day: ')
                elif mod_element_of_the_year[1] == 'help':
                    print(identify_the_date.__doc__)
                    mod_element_of_the_year[1] = input('\nEnter the month: ')
                elif i == 1:
                    print('\nEnter the integer, please!')
                    mod_element_of_the_year[i] = input('\nEnter the month: ')
                elif mod_element_of_the_year[0] == 'help':
                    print(identify_the_date.__doc__)
                    mod_element_of_the_year[0] = input('\nEnter the year: ')                    
                elif i == 0:
                    print('\nEnter the integer, please!')
                    mod_element_of_the_year[i] = input('\nEnter the year: ')
    return mod_element_of_the_year

from variator import variator as vari

# The crarion new class of data
class RepeaterSet:
    def create_set(*words):
        words = list(words)
        mod_words_set = set()
        for i in range(0, len(words), 1):
            mod_words = vari(words[i])
            mod_words_set = mod_words_set | mod_words
        return mod_words_set


# The body of the program
day = input('\nEnter the day: ')
elemaents_of_date = to_int(0, 0, day)
day = elemaents_of_date[2]
month = input('\nEnter the month: ')
elemaents_of_date = to_int(0, month, day)
month = elemaents_of_date[1]
year = input('\nEnter the year: ')
elemaents_of_date = to_int(year, month, day)
year = elemaents_of_date[0]
identify_the_date(year, month, day)

# The creation of the cycle to repeat the program
repeater_set = RepeaterSet
repeater_set = repeater_set.create_set('y', 'yes')
no_repeater_set = RepeaterSet
no_repeater_set = no_repeater_set.create_set('n', 'no')
other_answers_set = repeater_set | no_repeater_set
repeater = input('''\nYou want to check another date?
If you want to check another date enter Y/y(Yes/yes).
If you want to exit the program enter N/n(No/no): ''')

while not repeater in other_answers_set:
    print("\nSorry, your answer cann't be understan. Enter another answer!")
    repeater = input('''\nYou want to check another date?
If you want to check another date enter Y/y(Yes/yes).
If you want to exit the program enter N/n(No/no): ''')

while repeater in repeater_set:
    day = input('\nEnter the day: ')
    elemaents_of_date = to_int(0, 0, day)
    day = elemaents_of_date[2]
    month = input('\nEnter the month: ')
    elemaents_of_date = to_int(0, month, day)
    month = elemaents_of_date[1]
    year = input('\nEnter the year: ')
    elemaents_of_date = to_int(year, month, day)
    year = elemaents_of_date[0]
    identify_the_date(year, month, day)
    repeater = input('''\nYou want to check another date?
If you want to check another date enter Y/y(Yes/yes).
If you want to exit the program enter N/n(No/no): ''')
    while not repeater in other_answers_set:
        print("\nSorry, your answer cann't be understan. Enter another answer!")
        repeater = input('''\nYou want to check another date?
If you want to check another date enter Y/y(Yes/yes).
If you want to exit the program enter N/n(No/no): ''')
else:
    print('OK')
