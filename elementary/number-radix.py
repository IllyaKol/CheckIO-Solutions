def checkio(str_number, radix):
    sum = 0
    number_len = len(str_number)
    for i, digit_symbol in enumerate(str_number):
        digit = int_with_alphabet(digit_symbol)
        if digit >= radix:
            sum = -1
            break
        sum += digit * (radix ** (number_len - i - 1))
    return sum



def int_with_alphabet(symbol):
    symbol_num = ord(symbol)
    return symbol_num - 55 if symbol_num > 64 else symbol_num - 48

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"