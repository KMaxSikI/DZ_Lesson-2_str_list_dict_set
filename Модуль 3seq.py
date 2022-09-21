# Модуль 3


list1 = input('Введите элементы для 1-го списка: ').split()

list2 = input('Введите элементы для 2-го списка: ').split()


for i in list1 and list2:
    if list1.count(i) == list2.count(i):
        list1.remove(i)

print(list1)


