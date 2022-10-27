n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

b = [0] * n

for i in range(n):
    b[(i + k) % n] = a[i]

print(a)
print(b)