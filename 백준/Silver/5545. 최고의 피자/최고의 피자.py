#백준 5545 최고의 피자
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

a,b = map(int,input().split())
c = int(input())
lis =[]

for _ in range(n):
    lis.append(int(input()))

lis.sort(reverse=True)

cal = c # 칼로리
cost = a # 비용
ans = cal//cost

for i in range(n):
    tmp1 = cal + lis[i]
    tmp2 = cost + b
    tmp3 = tmp1//tmp2
    if tmp3 >= ans :
        ans = tmp3
        cal = tmp1
        cost = tmp2
    else :
        break

print(ans)


