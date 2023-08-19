"""
This program created to calculate the grand total of a bank account
after some years at a rate of 10 percent per annum of the amount.
User just need to enter the amount of bank account in special field
and enter numbers of the years of bank storage of a bank account amount.
If you need a help in usage of the special fiels,
enter "help".
"""

print(__doc__)

# Creation the function to calculate the value of a bank account
def bank_account(deposit_amount, years):
    y = 0
    grand_total = deposit_amount
    while y != years:
        grand_total = grand_total * 1.1
        y += 1
    return print('\nYour bank deposit of ${}, after {} years will be: {}$'
                 .format(deposit_amount, years, round(grand_total, 2)))

# Creation the function to modify the amount of a bank account
def to_float_amount(deposit_amount_to_mod):
    """
In this field you need to enter the amount of a bank account.
The amount should be enter in digital format and no more than 2-digit reminder in the end of
the number of the amount.
For example: 2110.23
"""
    while not type(deposit_amount_to_mod) is float:
        try:
            deposit_amount_to_mod = float(deposit_amount_to_mod)
            if deposit_amount_to_mod != round(deposit_amount_to_mod, 2):
                print('\nPlease. Enter the amount with 2-digit reminder')
                deposit_amount_to_mod = input('\nEnter the amount of the bank deposite: ')
            elif deposit_amount_to_mod < 0:
                print('\nPlease. Enter the amount which is greater than or equal to zero: ')
                deposit_amount_to_mod = input('\nEnter the amount of the bank deposite: ')
        except ValueError:
            # This is the condition to recall help
            if deposit_amount_to_mod == 'help':
                print(to_float_amount.__doc__)
                deposit_amount_to_mod = input('\nEnter the amount of the bank deposite: ')
            else:
                print("\nSorry, your answer cann't be understand. Please, try type again")
                deposit_amount_to_mod = input('\nEnter the amount of the bank deposite: ')    
    return deposit_amount_to_mod

# Creation the function to modify term of a the bank storage
def to_int_years(years_to_modify):
    """
In this field you need to enter the terms of storage of the bank account.
The terms should be enter in integer.
For example: 2
"""
    while not type(years_to_modify) is int:
        try:
            years_to_modify = int(years_to_modify)
            if years_to_modify < 0:
               print('\nPlease. Enter the number which is greater than or equal to zero: ')
               years_to_modify = input('\nEnter number of years of bank storage: ')
        except ValueError:
            # This is the condition to recall help
            if years_to_modify == 'help':
                print(to_int_years.__doc__)
                years_to_modify = input('\nEnter number of years of bank storage: ')
            else:
                print("\nSorry, your answer cann't be understand. Please, try type again")
                years_to_modify = input('\nEnter number of years of bank storage: ')        
    return years_to_modify

# Importing function to variate words from past programs
from variator import variator

# Creation the body of instructions of the program
amount = input('\nEnter the amount of the bank deposite: ')
amount = to_float_amount(amount)
years = input('\nEnter number of years of bank storage: ')
years = to_int_years(years)
bank_account(amount, years)

# Creation cycles to repeat realisation of program
repeater_set = variator('y') | variator('yes')
no_repeater_set = variator('n') | variator ('no')
other_answers_set = repeater_set | no_repeater_set
repeater = input('''\nDo you want to calculate another bank account?\n
Enter Y/y(Yes/yes) if you want to calculate
Enter N/n(No/no) if you want to exit: ''')

while not repeater in other_answers_set:
    print("\nSorry, your answer cann't be understand.")
    repeater = input('''\nDo you want to calculate another bank account?\n
Enter Y/y(Yes/yes) if you want to calculate
Enter N/n(No/no) if you want to exit: ''')

while repeater in repeater_set:
    amount = input('\nEnter the amount of the bank deposite: ')
    amount = to_float_amount(amount)
    years = input('\nEnter number of years of bank storage: ')
    years = to_int_years(years)
    bank_account(amount, years)
    repeater = input('''\nDo you want to calculate another bank account?\n
Enter Y/y(Yes/yes) if you want to calculate
Enter N/n(No/no) if you want to exit: ''')
    while not repeater in other_answers_set:
        print("\nSorry, your answer cann't be understand.")
        repeater = input('''\nDo you want to calculate another bank account?\n
Enter Y/y(Yes/yes) if you want to calculate
Enter N/n(No/no) if you want to exit: ''')
else:
    print('\nThank you for using this program!')
