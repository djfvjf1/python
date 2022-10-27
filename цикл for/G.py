x = int(input())

for i in range(2, 30000):
    if x % i == 0 & x !=1:
        print(i)
        break