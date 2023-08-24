# The creation of the function to encrypt words
def xor_cyphering(word_to_cyph, key_to_cyph):
    cyphered_word = ''
    word_to_cyph = list(word_to_cyph)
    key_to_cyph = list(key_to_cyph)
    for i in range(0, len(word_to_cyph), 1):
        word_to_cyph[i] = ord(word_to_cyph[i])
        for j in range(0, len(key_to_cyph), 1):
            word_to_cyph[i] = word_to_cyph[i] ^ ord(key_to_cyph[j])        
        word_to_cyph[i] = chr(word_to_cyph[i])
        cyphered_word += word_to_cyph[i]
    return cyphered_word
