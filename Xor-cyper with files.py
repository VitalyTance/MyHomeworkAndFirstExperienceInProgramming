"""
This program can encrypt and decrypt the words you want to.
If you want to encrypt the word you need to type "encrypt" in "What operation you want to do" field
If you want to decrypt the encrypted word you need to type "decrypt" in the same special field.
If you want to exit the program you need type "exit" in the same special field for this operation.
If you want to recall the documentation you need to type "help" in "What operation you want to do" field.
"""
# The creation of the class of new data
from variator import variator as vari

class RepeaterSet:
    def repeatering(*words):
        words = list(words)
        mod_words_set = set()
        for i in range(0, len(words), 1):
            mod_words = vari(words[i])
            mod_words_set = mod_words_set | mod_words
        return mod_words_set
    

# The body of the program

# The creation of set to continue or break program process
repeater_set = RepeaterSet
repeater_set = repeater_set.repeatering('y', 'yes')
no_repeater_set = RepeaterSet
no_repeater_set = no_repeater_set.repeatering('n', 'no')
other_answers_of_repeater_set = repeater_set | no_repeater_set

task_set = set(('encrypt', 'decrypt', 'exit', 'help'))

#The creation of condition to interact with the program
task = input('\nWhat operation you want to do(type "help" to call documentation): ')
while not task in task_set:
    task = input('\nWhat operation you want to do(type "help" to call documentation): ')
    
while task in task_set:
    if task == 'help':
        print(__doc__)
        task = input('\nWhat operation you want to do(type "help" to call documentation): ')
        while not task in task_set:
            task = input('\nWhat operation you want to do(type "help" to call documentation): ')
    elif task == 'encrypt':
        from xor_cyphering import xor_cyphering
        origin_word = input('\nEnter the word you want to encrypt: ')
        key_to_encrypt = input('\nEnter the encrypting key: ')
        with open('encrypted words.txt', 'a', encoding='ascii') as wrt_encr_wrd:
            wrt_encr_wrd.write((xor_cyphering(origin_word, key_to_encrypt) + '\n'))
            print('\nThe word encrypted and written in special text file')
        repeater = input('''\nDo you want to continue use the programm?
Enter Y/y(Yes/yes) to continue or N/n(No/no) to exit: ''')
        while not repeater in other_answers_of_repeater_set:
            print("\nSorry, your answer cann't be understand. Type again")
            repeater = input('''\nDo you want to continue use the programm?
Enter Y/y(Yes/yes) to continue or N/n(No/no) to exit: ''')
        if repeater in repeater_set:
            task = input('\nWhat operation you want to do(type "help" to call documentation): ')
        elif repeater in no_repeater_set:
            print('Thank you for using program')
            break
    elif task == 'decrypt':
        from xor_decyphering import xor_decyphering
        encrypted_word = input('\nEnter the word you want to decrypt: ')
        key_to_decrypt = input('\nEnter the decrypting key: ')
        print(('\n' + xor_decyphering(encrypted_word, key_to_decrypt)))
        repeater = input('''\nDo you want to continue use the programm?
Enter Y/y(Yes/yes) to continue or N/n(No/no) to exit: ''')
        while not repeater in other_answers_of_repeater_set:
            print("\nSorry, your answer cann't be understand. Type again")
            repeater = input('''\nDo you want to continue use the programm?
Enter Y/y(Yes/yes) to continue or N/n(No/no) to exit: ''')
        if repeater in repeater_set:
            task = input('\nWhat operation you want to do(type "help" to call documentation): ')
        elif repeater in no_repeater_set:
            print('Thank you for using program')
            break
    elif task == 'exit':
        break
    while not task in task_set:
        task = input('\nWhat operation you want to do(type "help" to call documentation): ')       
