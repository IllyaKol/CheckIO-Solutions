import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    count = 0
    text = text.upper()
    main_list = ['A', 'E', 'I', 'O', 'U', 'Y']
    words_splitted = re.split(' |,|\?|\.', text)
    for word in words_splitted:
        if len(word) < 2 or word == '':
            continue

        for i in range(len(word) - 1):
            if (word[i] in main_list) == (word[i + 1] in main_list) or word[i].isdigit():
                break
        else:
            count += 1

    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
