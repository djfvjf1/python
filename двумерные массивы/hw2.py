n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]

c = 0
for i in range(n):
    for j in range(len(a[i])):
        if a[i][j] == a[j][i]:
            c += 1


if c == n ** 2:
    print('yes')
else:
    print('no')

print(c)