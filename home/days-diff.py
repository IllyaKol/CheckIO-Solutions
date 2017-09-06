	import math
import datetime
def days_diff(date1, date2):
    if date1 == date2:
        return 0
    else:
        first = list(date1)
        first_string = ''.join(str(i) + ',' for i in first)
        first_string = first_string.split(',')
        first_date = datetime.date(int(first_string[0]), int(first_string[1]), int(first_string[2]))
        second = list(date2)
        second_string = ''.join(str(i) + ',' for i in second)
        second_string = second_string.split(',')
        second_date= datetime.date(int(second_string[0]), int(second_string[1]), int(second_string[2]))
        result = first_date - second_date
        result = str(result)
        result = result.split()[0]

        return abs(int(result))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
