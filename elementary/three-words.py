def checkio(words):
    word = words.split()
    if len(word) < 3:
        return False
    else:
        var = True
        for i in range(0, len(word) - 2):
            if word[i].isdigit() or word[i + 1].isdigit() or word[i + 2].isdigit():
                var = False
            else:
                var = True
                break
        return var
        

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"