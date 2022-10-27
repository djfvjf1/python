N = int(input())

zero = 0
pos = 0
neg = 0
for i in range(N):
    a = int(input())
    if a == 0:
        zero += 1
    elif a > 0:
        pos += 1
    elif a < 0:
        neg += 1
print(zero, pos, neg)