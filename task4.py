# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

def mnogochlen(file_name, k):
    with open(file_name, 'a', encoding='utf-8') as file_S:
        file_S.write(f'{random.randint(0, 100)}*x**{k}')

    for i in range(k - 1, 1, -1):
        with open(file_name, 'a', encoding='utf-8') as file_S:
            file_S.write(f' + {random.randint(0, 100)}*x**{i}')

    with open(file_name, 'a', encoding='utf-8') as file_S:
        file_S.write(f' + {random.randint(0, 100)}*x + {random.randint(0, 100)} = 0\n')


mnogochlen('mnogochlen1.txt', 5)
mnogochlen('mnogochlen2.txt', 8)
