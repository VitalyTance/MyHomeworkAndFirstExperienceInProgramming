def xor_decyphering(word_to_decrypt, key_of_cyph):
    decyphered_word = ''
    word_to_decrypt = list(word_to_decrypt)
    key_of_cyph = list(key_of_cyph)
    key_of_cyph.reverse()
    for i in range(0, len(word_to_decrypt), 1):
        word_to_decrypt[i] = ord(word_to_decrypt[i])
        for j in range(0, len(key_of_cyph), 1):
            word_to_decrypt[i] = word_to_decrypt[i] ^ ord(key_of_cyph[j])
        word_to_decrypt[i] = chr(word_to_decrypt[i])
        decyphered_word += word_to_decrypt[i]
    return decyphered_word
