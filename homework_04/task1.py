# Задание 1. Три списка
# Даны три списка.
# array_1 = [1, 5, 10, 20, 40, 80, 100]
# array_2 = [6, 7, 20, 80, 100]
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Нужно выполнить две задачи:
# 1. найти элементы, которые есть в каждом списке;
# 2. найти элементы из первого списка, которых нет во втором и третьем
# списках

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

new_array = array_1 + array_2 + array_3
new_num = []
not_num = []
for i in new_array:
    if i in array_1 and i in array_2 and i in array_3 and not i in new_num:
        new_num.append(i)
print(new_num)
for i in array_1:
    if i not in array_2 and i not in array_3:
        not_num.append(i)
print(not_num)