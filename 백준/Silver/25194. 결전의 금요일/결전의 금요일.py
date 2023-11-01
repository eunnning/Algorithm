#백준 25194 결전의 금요일

import sys
input = sys.stdin.readline

n = int(input())

work = list(map(int,input().split()))


dp = [0] * (7)
dp[0] = 1

for i in range(n):
    tmp = [0] * 7
    for j in range(7):
        if dp[j] == 1 :
            tmp[(work[i]+j)%7] = 1
            tmp[j] = 1
    dp = tmp


if dp[4] :
    print('YES')
else :
    print('NO')

