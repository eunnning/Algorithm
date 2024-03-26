#백준 17208 카우버거 알바생
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m,k = map(int, input().split())
lis = [[0,0]]

for _ in range(n):
    lis.append(list(map(int,input().split())))

lis.sort(key= lambda x : x[0]+x[1])

dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1,n+1):
    burger, fries = lis[i]
    for b in range(1,m+1):
        for f in range(1,k+1):
            if burger <= b and fries <= f :
                dp[i][b][f] = max(dp[i-1][b][f],dp[i-1][b-burger][f-fries]+1)
            else :
                dp[i][b][f] = dp[i-1][b][f]

print(dp[n][m][k])

