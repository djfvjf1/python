n = int(input())
d = {}

max = 0
for i in range(n):
    s = input().split() 
    for word in s:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
        # Находим максимальное значение в словаре и добавляем его в переменную max
        if d[word] > max:
            max = d[word]

for key, value in sorted(d.items()):
    if value == max:
        print(key)
        break

