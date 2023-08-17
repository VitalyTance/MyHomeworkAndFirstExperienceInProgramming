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
