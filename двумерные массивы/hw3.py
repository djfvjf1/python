n = [int(i) for i in input().split()] # n = 3 3 (информатикс)
a = [[0] * n[1] for i in range(n[0])] 



for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = i * j
        a[i][j] = str(a[i][j])

for d in range(len(a)): 
    s = " ".join(a[d]) 
    print(s) 
