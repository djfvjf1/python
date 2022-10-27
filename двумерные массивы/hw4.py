n = [int(i) for i in input().split()]
a = [[0] * n[1] for i in range(n[0])]

for i in range(len(a)):
    for j in range(len(a[i])):
       a[0][j] = 1
       a[i][0] = 1
       a[i][j] = a[i - 1][j] + a[i][j - 1]

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = str(a[i][j])
        
for d in range(len(a)):
    s = " ".join(a[d])
    print(s)
