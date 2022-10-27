n = int(input())
a = [[0] * n for i in range(n)]


for i in range(n): # Пробегаем по строкам
    a[i][- 1 - i] = 1 # Меняем противоположную диагональ с нулей на единицы
    for j in range(len(a[i])): 
        if j < i: 
            a[i][-1 -j] = 2 


for i in range(n): 

    for j in range(len(a[i])): 

        a[i][j] = str(a[i][j]) 
 

# Записываем массив в виде матрицы
for d in range(len(a)): 
    
    s = " ".join(a[d]) 
    print(s) 

