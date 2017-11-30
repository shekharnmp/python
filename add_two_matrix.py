"Python Program to Add Two Matrices"

a = [[1,2,3],
    [4,5,6],
    [7,8,9]]
b =[[1,4,3],
   [5,2,7],
   [9,6,8]]
r = [[0,0,0],
    [0,0,0],
    [0,0,0]]

for i in range(len(a)):
    for j in range(len (a[0])):
        r[i][j]=a[i][j]+b[i][j]
        
print r
for c in r:
    print c
