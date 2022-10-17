# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# def getSum (number):
#     sum = 0
#     for i in number:
#         if i != '.':
#             sum = sum + int(i)
#     return sum
#
# number = input('Введите вещественное число: ' )
#
# print (f'Сумма цифр равна: {getSum(number)}')

print(f"Сумма цифр равна: {sum(list(map(lambda a: 0 if a == '.' else int(a), input('Введите вещественное число: '))))}")