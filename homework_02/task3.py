# Задача 3. Игра «Угадай число»
# Папа-программист написал для сына программу, которая просит его угадать
# число. Недостаток программы был в том, что бедному сыну приходилось её
# каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем
# гораздо больше, пришло время исправить этот недостаток и заодно немного
# улучшить саму игру.
# Напишите программу-игру, которая запрашивает у пользователя число до тех
# пор, пока он его не отгадает.

num = int(input('Загадайте и введите число от 0 до 20 :'))
flag = True
while flag == True:
    num_user = int(input('Введите число от 0 до 20 :'))
    if num_user > num:
        print("Введенное число больше загаданного. Попробуй еще.")
    elif num_user < num:
        print("Введенное число меньше загаданного. Попробуй еще.")
    elif num_user == num:
        print("Молодец. Угадал")
        flag = False

