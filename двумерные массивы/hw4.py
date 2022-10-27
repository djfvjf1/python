n = [int(x) for x in input().split()]
a = [[0] * int(n[1]) for i in range(n[0])]

for i in range(n):
    for j in range(len(a[i])):
        a[i][j]=a[i-1][j]+a[i][j-1]


for i in range(n): 

    for j in range(len(a[i])): 

        a[i][j] = str(a[i][j]) 
 

# Записываем массив в виде матрицы
for d in range(len(a)): 
    
    s = " ".join(a[d]) 
    print(s) 