"""
Now, you can type in this programm the numbers you want to be operated by operands
which can by written durint programm's realisation.
After, you need to choose one of the four mathematic actions
you want to realise by typing in windows or console -
"+" for sum, "--" for substruction, "*" for multiply and "/" for deviding.
"""
print(__doc__)


# For begining, creat arithmetic function with 3 arguments (1-st number, 2-nd number and operation)
def arithmetic(operation):
    """
Actually, this is the pointing of operation programm need realise
"""
    def calculator(number_1, number_2):
        if operation == '+':
            c = number_1 + number_2
            print(c)
        elif operation == '--':
            c = number_1 - number_2
            print(c)
        elif operation == '*':
            c = number_1 * number_2
            print(c)
        elif operation == '/':
            try:
                c = number_1 / number_2
                print(c)
            except ZeroDivisionError:
                print("It's Zero Division")
            
        else:
            print('Unknown operation')
    return calculator

def floating(c_number):
    while not type(c_number) is float:
        try:
            c_number = float(c_number)
        except ValueError:
            print('Need a number: ')
            c_number = input('Enter the number: ')
    return c_number


# Now, creat programm arguments to operate
number_1 = input("Enter the 1st number: ")
number_1 = floating(number_1)
number_2 = input("Enter the 2nd number: ")
number_2 = floating(number_2)
print(arithmetic.__doc__)
operation = str(input('What operation do you want to realise: '))
calculation = arithmetic(operation)
calculation(number_1, number_2)
#Command to repeat the cycle of algorithmic operation
repeater = str(input('To repeat?: '))
# Creat the tuple to repeat the cycle of algorithmic operations
repeater_tuple = ('Y', 'y', 'Yes', 'yes')
# Creat the tuple to break the cycle of algorithmic operations
no_repeater_tuple = ('N', 'n', 'No','no')
readable_answers_tuple = repeater_tuple + no_repeater_tuple

while not repeater in readable_answers_tuple:
    print('Sorry, enter another value!')
    repeater = str(input('To repeat?: '))


# Now create the cycle of repeating of arithmetic operations
# If user answer 'Y' or 'y' or "yes" the cycle gonna be repeat
while repeater in repeater_tuple:
    number_1 = input("Enter the 1st number: ")
    number_1 = floating(number_1)
    number_2 = input("Enter the 2nd number: ")
    number_2 = floating(number_2)
    operation = str(input('What operation do you want to realise: '))
    calculation = arithmetic(operation)
    calculation(number_1, number_2)
    repeater = str(input('To repeat?: '))
    # If user doesn't type something existional as 'yes' or 'no' and written variations
    while not repeater in readable_answers_tuple:
        print('Sorry, enter another value!')
        repeater = str(input('To repeat?: '))
else:
    print('OK')
