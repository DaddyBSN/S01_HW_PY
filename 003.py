# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка .
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

print("Enter x: ")
x = int(input())

print("Enter y: ")
y = int(input())

if (x>0):
    if(y>0):
        print("1 четверть")
    if(y<0):
        print("4 четверть")
if (x<0):
    if(y<0):
        print("3 четверть")
    if(y>0):
        print("2 четверть")