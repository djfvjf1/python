N = int(input())

c = 0
for i in range(N):
    a = int(input())
    if a % 10 == 0 or a == 0:
        c += 1
print(c)