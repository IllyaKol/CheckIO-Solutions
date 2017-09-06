def verify_anagrams(first_word, second_word):
    first_word = first_word.replace(' ', '')
    second_word = second_word.replace(' ', '')

    first_words = list(first_word.lower())
    second_words = list(second_word.lower())

    if len(first_words) != len(second_words):
        return False


    for letter in second_words:
        if letter in first_words:
            first_words.remove(letter)
    if len(first_words) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

