a = int(input())
b = int(input())

for i in range(a, b):
    for j in range(a, b):
        if i == j**2:
            print(i)
    