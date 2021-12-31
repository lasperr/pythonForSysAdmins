'''Print an n×n table filled with numbers from 1 to n^2 
in a spiral coming out of the upper left corner and twisted clockwise'''

n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
k = 1 
m = 0 
while k <= n*n: 
    for i in range(m, n-m): 
        a[m][i]= k
        k += 1
    for i in range(m+1, n-m): 
        a[i][n-m-1]= k
        k += 1
    for i in range(n-m-2, m-1, -1):
        a[n-m-1][i] = k
        k += 1
    for i in range(n-2-m,m, -1): 
        a[i][m] = k
        k += 1
    m += 1
for i in range(n): 
    for j in range(n):
        print(a[i][j], end =' ')
    print()