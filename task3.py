"""
Данные, функции и модули в Python
3.1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

# from random import *

# n = int(input("Введите количество элементов в массиве: "))
# my_list = []
# for i in range(n):
#     my_list.append(randint(0, 100))
# print(my_list)
# print(my_list[1::2])
# print(sum(my_list[1::2]))


"""
3.2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""


# from random import *
# n = int(input("Введите количество элементов в массиве: "))
# my_list = []
# for i in range(n):
#     my_list.append(randint(0, 100))
# print(my_list)

# r_list = []
# for i in range(n // 2 + 1):
#     r_list.append(my_list[i] * my_list[-i - 1])
#     print(f'{i + 1} : {my_list[i]} * {my_list[-i -1]}')
# print('Произведение чисел >>> ', r_list)


"""
3.3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)
# print(max-min)

"""
3.4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное >>> "))
# while n != 0:
#     s = str(n % 2) + s
#     n //= 2
# print('Ответ >>> ', s)

"""
3.5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0
%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0
%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0
%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81
D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D
1%87%D0%B8.)
- [Фибоначчи] (https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0
%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0
%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1
%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0
%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)
"""

# k = int(input("Inset k: "))

# fibonacciList = [0]*(k*2+1)
# fibonacciList[k] = 0
# fibonacciList[k+1] = 1

# for i in range(k+2, len(fibonacciList)):
#     fibonacciList[i] = fibonacciList[i-2]+fibonacciList[i-1]

# for i in range(k, -1, -1):
#     fibonacciList[i] = fibonacciList[i+2]-fibonacciList[i+1]

# print(fibonacciList)

########################


# def Fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)


# def NegaFibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2


# list = [0]
# userNumber = int(input('Введите число >>> '))
# for e in range(1, userNumber + 1):
#     list.append(Fibonacci(e))
#     list.insert(0, NegaFibonacci(e))
# print(list)
