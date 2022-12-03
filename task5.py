with open('mnogochlen1.txt', 'r', encoding='utf-8') as file_S:
    a = file_S.read()
with open('mnogochlen2.txt', 'r', encoding='utf-8') as file_S:
    b = file_S.read()


def odnochlen(list_M):
    list_M = list_M.replace(' ', '')
    list_a = []
    start = 0
    for index, i in enumerate(list_M):

        if i == '+' or i == '-':
            list_a.append(list_M[start:index])
            start = index
    list_a.append(list_M[start:])
    list_a[-1] = list_a[-1].replace('=0\n', '')
    return list_a

list_A = odnochlen(a)
List_B = odnochlen(b)


def magic(l_a, l_b):
    list_resault = list(zip(l_a[::-1], l_b[::-1]))[::-1]
    d = abs(len(l_a) - len(l_b))
    if len(l_a) > len(l_b):
        for i in l_a[d - 1::-1]:
            list_resault.insert(0, i)
    elif len(l_a) < len(l_b):
        for i in l_b[d - 1::-1]:
            list_resault.insert(0, i)

    end_resault = []
    for i in list_resault:
        if len(i) != 2:
            end_resault.append(i)
        else:
            i = list(i)
            if len(i[0].split('*')) > 1:
                l = int(i[0].split('*')[0])
                m = int(i[1].split('*')[0])
                c = l + m
                inx = i[0].find('*')
                x = i[0][inx + 1:]
                end_resault.append(f'{c}*{x}')
            else:
                end_resault.append(str(int(i[0]) + int(i[1])))
    for i in range(1, len(end_resault)):

        if end_resault[i][0] == '-' or end_resault[i][0] == '+':
            end_resault[i] = end_resault[i].replace('-', ' - ')
            end_resault[i] = end_resault[i].replace('+', ' + ')
        else:
            end_resault[i] = ' + ' + end_resault[i]
    end_resault = ''.join(end_resault) + ' = 0'

    with open('sum_mnogochlen.txt', 'a', encoding='utf-8') as file_S:
        file_S.write(f'{end_resault}')


magic(list_A, List_B)





