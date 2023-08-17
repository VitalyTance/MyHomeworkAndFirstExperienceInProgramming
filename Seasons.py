"""
This program specialized to determine the season of an year by month,
typed by user.
To get the season the month is a part of user need to enter the number or
first 3 letter of the necessary month.
The number should be enter in digital format.
For instruction, enter
"help" in "Enter a number or 3 first letter" field.
"""
print(__doc__)

# Creation the function to determine the season of an year
from variator import variator
def season(month):
    """
You can enter the number of the month in digital format(for example: 1 or 01).
Or you can enter 3 first letters of the choosen month(for example: jan)
"""
    winter = variator('dec') | variator('jan') | variator ('feb') | set(('1', '2', '12', '01', '02'))
    spring = variator('mar') | variator('apr') | variator ('may') | set(('3', '03', '4', '04', '5', '05'))
    summer = variator('jun') | variator('jul') | variator ('aug') | set(('6', '06', '7', '07', '8', '08'))
    autumn = variator('sep') | variator('oct') | variator ('nov') | set(('9', '09', '10', '11'))
    an_year = winter | spring | summer | autumn
    while not month in an_year:
        # This is the condition to recall help for user
        if month == 'help':
            print(season.__doc__)
            month = input ("""Enter a number or 3 first letters
of the month you want to determine: """)
        else:
            print("\nSorry, your request cann't be understand. Please, try again\n")
            month = input ("""Enter a number or 3 first letters
of the month you want to determine: """)
    else:
        if month in winter:
            print('\nWinter')
        elif month in spring:
            print('\nSpring')
        elif month in summer:
            print('\nSummer')
        elif month in autumn:
            print('\nAutumn')

   
#The body of program determine the season of an year
name_or_number_of_a_month = input ("""Enter a number or 3 first letters
of the month you want to determine: """)
season(name_or_number_of_a_month)

repeater_set = variator('y') | variator('yes')
no_repeater_set = variator('n') | variator('no')
other_answers_set = repeater_set | no_repeater_set
repeater = input("""\nDo you want to repeat this program?
Please, enter Y/y(Yes/yes) to repeat or N/n(No/no) to end: """)
# The cycle to repeat the program while user enter request "Yes"
while not repeater in other_answers_set:
    print("\nSorry, your request cann't be understand. Please, try again")
    repeater = input("""\nDo you want to repeat this program?
Please, enter Y/y(Yes/yes) to repeat or N/n(No/no) to end: """)
while repeater in repeater_set:
    name_or_number_of_a_month = input ("""\nEnter a number or 3 first letters
of the month you want to determine: """)
    season(name_or_number_of_a_month)
    repeater = input("""\nDo you want to repeat this program?
Please, enter Y/y(Yes/yes) to repeat or N/n(No/no) to end: """)
    while not repeater in other_answers_set:
        print("\nSorry, your request cann't be understand. Please, try again")
        repeater = input("""\nDo you want to repeat this program?
Please, enter Y/y(Yes/yes) to repeat or N/n(No/no) to end: """)
else:
    print("\nProgram has ended")    
