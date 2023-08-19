"""
This programm calculate 3 values related to the geometrical figure
called "square". Where 3 values calculated by this programm -  the area, the sum of the lengths and the diagonal of the square.
To calculate that values you need to enter the lenght of the square you want to operate with.
The lenght should be typed in digital format.
"""

# This function to calculate 3 values (area, the sum of the lengths, diagonal) of a square
def square(square_side):
    import math
    result_of_realisation_square_func = []
    the_sum_of_the_lengths = square_side * 4
    result_of_realisation_square_func.append(the_sum_of_the_lengths)
    area_of_the_square = square_side ** 2
    result_of_realisation_square_func.append(area_of_the_square)
    the_diagonal = math.sqrt (2 * (square_side**2))
    result_of_realisation_square_func.append(the_diagonal)
    result_of_realisation_square_func = tuple(result_of_realisation_square_func)
    return result_of_realisation_square_func

# This function transform user tiped data to float number
def floating(square_side_to_transform):
    while not type(square_side_to_transform) is float:
        try:
            square_side_to_transform = float(square_side_to_transform)
            if square_side_to_transform <= 0:
                print('Please, enter the value which is greater than zero')
                square_side_to_transform = input("Enter the length of the square side: ")
        except:
            print('Plese, type the number')
            square_side_to_transform = input("Enter the length of the square side: ")       
    return square_side_to_transform

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


print(__doc__)
# This is the body of the programm contains the instractions
side_of_square_to_check = input("Enter the length of the square side: ")
side_of_square_to_check = floating(side_of_square_to_check)
square(side_of_square_to_check)
print(square(side_of_square_to_check))

repeater_set = variator('yes') | variator ('y')
no_repeater_set = variator('no') | variator ('n')
other_repeater_answers = repeater_set | no_repeater_set
repeater = input("""To repeat?\n
If you want to repeat enter Y/y (Yes/yes) or N/n (No/no): """)

while not repeater in other_repeater_answers:
    print('Sorry, your answer is unknown. Please, enter your answer again')
    repeater = input("""To repeat?\n
If you want to repeat enter Y/y (Yes/yes) or N/n (No/no): """)
    
while repeater in repeater_set:
    side_of_square_to_check = input("Enter the length of the square side: ")
    side_of_square_to_check = floating(side_of_square_to_check)
    square(side_of_square_to_check)
    print(square(side_of_square_to_check))
    repeater = input("""To repeat?\n
If you want to repeat enter Y/y (Yes/yes) or N/n (No/no): """)
    while not repeater in other_repeater_answers:
        print('Sorry, your answer is unknown. Please, enter your answer again')
        repeater = input("""To repeat?\n
If you want to repeat enter Y/y (Yes/yes) or N/n (No/no): """)   
else:
    print('OK')
