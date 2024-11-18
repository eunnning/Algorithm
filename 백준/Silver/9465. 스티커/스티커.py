#백준 9465 스티커
import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())

for _ in range(t):
    n = int(input())
    lis = [list(map(int, input().split())) for _ in range(2)]
    lis = [[0] + i for i in lis]
    dp = [[0] * (n+1) for _ in range(2)]

    dp[0][1] = lis[0][1]
    dp[1][1] = lis[1][1]

    for j in range(2,n+1):
        dp[0][j] = max(dp[1][j-1],dp[1][j-2]) + lis[0][j]
        dp[1][j] = max(dp[0][j-1],dp[0][j-2]) + lis[1][j]

    print( max(map(max, dp)))

    