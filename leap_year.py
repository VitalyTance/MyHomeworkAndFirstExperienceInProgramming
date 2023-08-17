"""
This program determines if the year is high or not.
To determine you need to type the year in digital format in special field.
After you enter digital value of the year program give you an answer
this year high or not.
If the year is high program give the answer "Yes".
If hte year is low program give the answer "No".
"""
print(__doc__)


# Creation a function to determ a leap year
def is_year_leap(chosen_year):
    leap_years_in_future = [year for year in range(2024, 1000000, 4)]
    leap_years_in_past = [year for year in range(2024, -10000000, -4)]
    leap_years = leap_years_in_future + leap_years_in_past
    leap_years = tuple(leap_years)
    if chosen_year in leap_years:
        print('Yes')
    else:
        print('No')

# Creation a function to correct user to type year in numbers not in letters or symbols
def inting(year_to_int):
    while not type(year_to_int) is int:
        try:
            year_to_int = int(year_to_int)
        except ValueError:
            print('Sorry, your data is unknown! Try again!')
            year_to_int = input('''Is this year high or not?\n
Enter the year in digital format: ''')
    return year_to_int
        

year_to_check = input('''Is this year is high or not?\n
Enter the year in digital format: ''')
year_to_check = inting(year_to_check)
is_year_leap(year_to_check)

repeater_tuple = ('Yes', 'yes', 'y', 'Y')
no_repeater_tuple = ('No', 'no', 'N', 'n')
other_repeater_answers = repeater_tuple + no_repeater_tuple
repeater = input('''Do you want to check another year?\n
Enter Y/Yes or N/No ''')

while not repeater in other_repeater_answers:
    print("Sorry, your answer is cann't be understand by the program!")
    repeater = input('''Do you want to check another year?\n
Enter Y/Yes or N/No ''')

while repeater in repeater_tuple:
    year_to_check = input('''Is this year high or not?\n
Enter the year in digital format: ''')
    year_to_check = inting(year_to_check)
    is_year_leap(year_to_check)
    repeater = input('''Do you want to check another year?\n
Enter Y/Yes or N/No ''')    
    while not repeater in other_repeater_answers:
        print("Sorry, your answer is cann't be understand by the program!")
        repeater = input('''Do you want to check another year?\n
Enter Y/Yes or N/No ''')
else:
    print("OK")
