n, m = map(int, input().split() )

a = []
for i in range(n) :
    row = list(map(int, input().split() ) ) 
    a.append(row)
    
b = []
for i in range(n):
    row = list(map(int, input().split() ) )
    b.append(row)

c = []
for i in range(n) :  
    matrix = []
    for j in range(m) :
        matrix.append(a[i][j] + b[i][j])
    c.append(matrix)

for i in c :
    print(' '.join(map(str, i)))
        