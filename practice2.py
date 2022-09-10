# answer = input('Какой язык программирования мы изучаем?')
# if answer == 'Python':
#     print('Верно! Мы ботаем Python =)')
#     print('Python - отличный язык!')
# else:
#     print('Не совсем так!')


# num = int(input())
# last_digit = num % 10    # последняя цифра числа
# first_digit = num // 10  # первая цифра числа

# if last_digit == first_digit:
#     print('ДА')
# else:
#     print('НЕТ')


# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)


# i = int(input())
# b = i % 2
# print(b)

# if i % 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
#
# n = int(input())
# for i in range(n, ):
#     print(i)


# pass1, pass2 = input('Веедите пароль: '), input('Повторите пароль: ')
# if pass1 == pass2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')


# a = int(input())
# b = a % 2
# if b == 0:
#     print('Yas')
# else:
#     print('No')

# print('Четное'if int(input()) % 2 == 0 else 'Нечетное')


# abcd = int(input())
# a = abcd // 1000
# b = abcd // 100 % 10
# c = abcd // 10 % 10
# d = abcd % 10
# if a + d == d - c:
#     print('ДА')
# else:
#     print('НЕТ')

# agePeople = int(input())
# if agePeople >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# a, b, c = int(input()), int(input()), int(input())
# if b-a == c-b:
#     print('YES')
# else:
#     print('NO')

# a, b = int(input()), int(input())
# if a < b:
#     print(a)
# else:
#     print(b)

# a, b = int(input()), int(input()),
# print(a if a < b else b)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a < b:
#     ab = a
# else:
#     ab = b
# if c < d:
#     cd = c
# else:
#     cd = d
# if ab < cd:
#     abcd = ab
# else:
#     abcd = cd
# print(abcd)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# z = max(a, b, c, d)
# print(z)

# print('Четное'if int(input()) % 2 == 0 else 'Нечетное')

# age = int(input())
# if age <= 13:
#     print('детство')
# elif age <= 24:
#     print('молодость')
# elif age <= 59:
#     print('зрелость')
# else:
#     age >= 60
#     print('старость')

# a, b, c = int(input()), int(input()), int(input())
# if a >= 0:
#     num1 = a
# else:
#     num1 = 0
# if b >= 0:
#     num2 = b
# else:
#     num2 = 0
# if c >= 0:
#     num3 = c
# else:
#     num3 = 0
# print(num1 + num2 + num3)

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('\nLine \n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('Line1 \n')
#     data.write('Line2 \n')


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()

# import practice1 as p
# print(new_string)

num1 = int(input('Введите 1 число: '))
num2 = int(input('Введите 2 число: '))

if num1 % num2:
    print('Не кратно, остаток', num1 % num2)
else:
    print('Кратно')
