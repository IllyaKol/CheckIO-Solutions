import re
def checkio(text):
    text = text.replace(' ', '').lower()
    text = re.sub(r'!|,|\.|-|\d', '', text)


    new_text = set(text)
    if len(new_text) != len(text):
        count = 0
        letter = []
        for i in text:
            if text.count(i) > count:
                letter = []
                count = text.count(i)
                letter.append(i)
            elif text.count(i) == count:
                count = text.count(i)
                letter.append(i)
        letter.sort()
        return letter[0]
    else:
        text = list(text)
        text.sort()
        return text[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
