# Задача 2. Часы
# Напишите программу, которая получает на вход число n (количество минут),
# затем считает, сколько это будет в часах и сколько минут останется, и выводит
# на экран эти два результата.
n = int(input())
hour = n // 60
min = n % 60
print(f"Часов: {hour}, минут: {min}")