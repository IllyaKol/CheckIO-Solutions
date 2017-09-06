FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    main_string = ''
    dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
           'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
           'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
           'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}

    if len(str(number)) == 3:
        result = number // 100
        main_string += search_key(dic, result)
        main_string += ' hundred'
        result = number % 100
        if (result > 20) and (result != 30) and (result != 40) and (result != 50) and (result != 60) and (result != 70) and (result != 80) and (result != 90):
            units = result % 10
            dozents = result - units
            main_string += ' '
            main_string += search_key(dic, dozents)
            main_string += ' '
            main_string += search_key(dic, units)
        elif result != 0:
            main_string += ' '
            main_string += search_key(dic, result)
    elif (20 < number < 99) and (number != 30) and (number != 40) and (number != 50) and (number != 60) and (number != 70) and (number != 80) and (number != 90):
        units = number % 10
        dozents = number - units
        main_string += search_key(dic, dozents)
        main_string += ' '
        main_string += search_key(dic, units)
    else:
        main_string += search_key(dic, number)
    return main_string

def search_key(dic, value):
    for key, val in dic.items():
        if val == value:
            return key


checkio(140)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
