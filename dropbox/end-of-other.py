def checkio(x):
    result = False
    if len(x) > 1:
        for main_word in x:
            main_word = main_word[::-1]
            for word in x:
                word = word[::-1]
                if main_word == word:
                    continue
                num = min(len(main_word), len(word))
                if main_word[:num] == word[:num]:
                    result = True
    return result



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"