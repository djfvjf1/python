a = [int(x) for x in input().split()]


for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            t = a[j + 1]
            a[j + 1] = a[j]
            a[j] = t
            print(a)