import math
def checkio(a, b, c):
    numbers = [a, b, c]
    maximum = max(numbers)
    minimum = min(numbers)
    angles = []
    if a == b and b == c and c == a:
        angles = [60, 60, 60]
    elif ((a + b + c) - maximum) <= maximum:
        angles = [0, 0, 0]
    else:
        angles = [search_angle(a, b, c), search_angle(a, c, b), search_angle(c, b, a)]


    angles.sort()
    return angles


def search_angle(a, b, c):
    cos_angle = float((a ** 2) + (b ** 2) - (c ** 2)) / float(2 * a * b)
    # print cos_angle
    arc_angle = math.acos(cos_angle)
    degree = round(math.degrees(arc_angle))
    # print degree
    return degree

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
