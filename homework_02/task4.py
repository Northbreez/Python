# Задача 4. Посчитай чужую зарплату...
# Бухгалтер устала постоянно считать вручную среднегодовую зарплату
# сотрудников компании и, чтобы облегчить себе жизнь, обратилась к
# программисту.
# Напишите программу, которая принимает от пользователя зарплату сотрудника
# за каждый из 12 месяцев и выводит на экран среднюю зарплату за год.

cash = 0
average_cash = 0
total_mount = 1
while total_mount != 13:

    cash += int(input("Введите сумму зарплаты :"))
    average_cash = cash / total_mount
    total_mount += 1
    if total_mount == 13:
        break
print(f'Средняя зарплата {average_cash} рублей')