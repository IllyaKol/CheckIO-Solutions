directions = [(1, 0), (1, 1), (-1, 0), (-1, -1), (0, 1), (-1, 1), (0, -1), (1, -1)]
def checkio(land_map):
    land_map.insert(0, [0] * len(land_map[0]))
    land_map.append([0] * len(land_map[0]))

    for i in range(len(land_map)):
        land_map[i].insert(0, 0)
        land_map[i].append(0)

    number = 2
    for row in range(1, len(land_map) - 1):
        for col in range(1, len(land_map[row]) - 1):
            if land_map[row][col] == 1:
                coordinates(row, col, land_map, number, directions)
                number += 1

    all_numbers = [j for i in land_map for j in i]

    maximum = max(all_numbers)
    minimunm = min(all_numbers)

    count_islands = []

    for r in range(minimunm, maximum + 1):
        if r > 1:
            a = all_numbers.count(r)
            count_islands.append(a)
    
    count_islands.sort()

    return count_islands


def coordinates(x, y, land_map, number, directions):
    land_map[x][y] = number
    for i in range(len(directions)):
        if land_map[x + directions[i][0]][y + directions[i][1]] == 1:
            coordinates(x + directions[i][0], y + directions[i][1], land_map, number, directions)



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
