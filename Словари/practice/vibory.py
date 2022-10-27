from array import array


n = int(input())

d = {}


for j in range(n):
    key, val = input().split()
    if key in d:
        d[key] += int(val)
    else:
        d[key] = int(val)

array = d.keys() # получаем ключи

array = list(array) # превращаем его в обычный список

#array.sort() # сортируем список

for i in array: # вывод элементов словаря по алфавиту
    print(i, d[i])