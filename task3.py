# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

P = [1, 1, 1, 3, 3, 5, 7, 7, 7, 9, 9, 11]

list_unikum = []
for i in P:
    if i not in list_unikum:
        list_unikum.append(i)


print(list_unikum)