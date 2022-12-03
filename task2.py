# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import random

N = random.randint(10, 1000)
print(f'Число N = {N}')

list_resault = []
for i in range(1, N + 1):
    if N % i == 0:
        list_resault.append(i)


print(list_resault)