# Модуль 1

list1 = []
a = int(input('Введите колличество элементов: ', ))

for i in range(1, a + 1):
    b = int(input(f'Введите {i} элеинтов: '))
    list1.append(b)

print(sorted(list1))
