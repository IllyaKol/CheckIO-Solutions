def recall_password(ciphered_password, cipher_grille):
    list_password = []
    string = ''
    for x in range(4):
        for i in range(len(ciphered_password)):
            for j, c in enumerate(ciphered_password[i]):
                if c == 'X' or c == 'x':
                   list_password.append(cipher_grille[i][j])
    
        new_list = [[], [], [], []]
        n = 0
        for y in range(4):
            for l in ciphered_password[::-1]:
                new_list[n].append(l[n])
            n += 1
        ciphered_password = new_list
        string = ''.join(list_password)
    return string
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

