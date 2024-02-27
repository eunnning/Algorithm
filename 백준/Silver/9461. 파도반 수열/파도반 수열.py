#백준 9461 파도반 수열
import sys
input = lambda: sys.stdin.readline().rstrip()


T = int(input())

lis = [0] * (100)

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + lis

for i in range(11,101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(T):
    x = int(input())
    print(dp[x])
