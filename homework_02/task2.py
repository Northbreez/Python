# Задача 2. Обычный день на работе
# Максим программирует целый день на работе и вечером идёт домой. Каждый час
# начальство кидает ему несколько задач, которые нужно решить до следующего
# рабочего часа. Вдобавок каждый час Максиму звонит супруга. Он знает, что если он
# возьмёт трубку, то жена попросит зайти вечером в магазин.
# Напишите программу, в которой считается, сколько задач выполнил Максим за день
# (восемь часов). Если он хотя бы раз взял трубку, то в конце дополнительно выводите
# сообщение: «Нужно зайти в магазин».

count_task = 0
count_wife = 0
hour = 8
while hour != 0:
    count_task += int(input("Введите количество задач:"))
    print('Звонит супруга. Взять трубку?')
    if int(input("'Да' - введите 1; 'Нет' - введите 0 :")) == 1:
        count_wife += 1
    hour -= 1
print(f'За день Максим решил {count_task} задач')
if count_wife > 1:
    print(("Нужно зайти в магазин"))