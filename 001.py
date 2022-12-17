# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

print('Enter day number: ')
day = int(input())

if (day > 7 or day < 1):
    print("It's not a day of the week")
if (day == 6 or day == 7):
    print("It's the weekend")
if (day >= 1 and day <= 5):
    print("It's not the weekend")