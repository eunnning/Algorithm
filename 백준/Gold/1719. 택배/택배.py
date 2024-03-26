#백준 1719 택배
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int,input().split()) 
lis = [[1e9]*(n+1)for _ in range(n+1)]
ans = [[j for j in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split()) 
    lis[a][b] = c
    lis[b][a] = c

for i in range(1,n+1):
    lis[i][i] = 0
    ans[i][i] = '-' 

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if lis[i][j] > lis[i][k]+lis[k][j] :
                lis[i][j] = lis[i][k]+lis[k][j]
                ans[i][j] = ans[i][k]

for i in range(1,n+1):
    for j in range(1,n+1):
        print(ans[i][j],end=' ')
    print()
