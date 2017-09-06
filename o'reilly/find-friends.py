def check_connection(network, first, second):
    dic ={}
    all_relatives = []
    for i in list(network):
        i = i.split('-')
        all_relatives.append(i)

    names = set()
    for name in all_relatives:
        names.add(name[0])
        names.add(name[1])

    dic = dict(zip(names, range(len(names))))

    first = dic[first]
    second = dic[second]

    matrix = []
    for i in range(len(names)):
        matrix.append([0] * len(dic))

    for i in all_relatives:
        first_number = dic[i[0]]
        second_number = dic[i[1]]
        matrix[first_number][second_number] = matrix[second_number][first_number] = 1

    vertices = set()

    return search_item(matrix, first, second, vertices)
    

def search_item(matrix, current_vertice, final_vertice, vertices):
    vertices.add(current_vertice)
    if current_vertice == final_vertice:
        return True
    for i in range(len(matrix[current_vertice])):
        if matrix[current_vertice][i] == 1 and i not in vertices:
            matrix[current_vertice][i] = 2
            result = search_item(matrix, i, final_vertice, vertices)
            if result:
                return result
    return False





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
