# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math
print("Enter the coordinates A x")
xA = float(input())
print("Enter the coordinates A y")
yA = float(input())

print("Enter the coordinates B x")
xB = float(input())
print("Enter the coordinates B y")
yB = float(input())

distance = round(math.sqrt((xB - xA)**2 + (yB - yA)**2), 3)
print(distance)