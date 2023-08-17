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
    leap_year = chosen_year % 4
    if leap_year == 0:
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

# Creation the function to variate of the word represented in list
def variator(word):
    list_of_variated_words = []
    for i in range(0, len(word)):
        variated_word = word[0:i] + word[i].swapcase() + word[i+1:len(word)]
        list_of_variated_words.append(variated_word)
    for i in range(1, len(word)+1):
        c_variated_word = word[0:i].swapcase() + word[i:len(word)]
        list_of_variated_words.append(c_variated_word)
    for i in range(1, len(c_variated_word)+1):
        l_variated_word = c_variated_word[0:i].swapcase() + c_variated_word[i:len(c_variated_word)]
        list_of_variated_words.append(l_variated_word)
    return set(list_of_variated_words)
        
# The body of programm, contains instructions to oerate with user's typing data
year_to_check = input('''Is this year is high or not?\n
Enter the year in digital format: ''')
year_to_check = inting(year_to_check)
is_year_leap(year_to_check)

repeater_set = variator('yes') | variator('y')
no_repeater_set = variator('n') | variator('no') 
other_repeater_answers = repeater_set | no_repeater_set
repeater = input('''Do you want to check another year?\n
Enter Y/Yes or N/No ''')

while not repeater in other_repeater_answers:
    print("Sorry, your answer is cann't be understand by the program!")
    repeater = input('''Do you want to check another year?\n
Enter Y/Yes or N/No ''')

while repeater in repeater_set:
    year_to_check = input('''Is this year is high or not?\n
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
    print('OK')
