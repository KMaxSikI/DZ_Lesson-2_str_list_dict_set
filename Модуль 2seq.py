# Модуль 2
import re

a = input()

re.split(',|;|/', a)

b = []

for i in a:
    if a.count(i) == 1:
        b.append(i)

print(b)
