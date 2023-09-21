#백준 2141 우체국

import sys
input = sys.stdin.readline

n = int(input())
lis=[]
summ = 0
for _ in range(n):
    a, b = (map(int, input().split()))
    lis.append([a,b])
    summ+=b

if summ == 0:
    print(-1000000000)
    exit()


lis.sort(key= lambda x: x[0])

ans = 0

for i in range(n):
    ans +=lis[i][1]
    if ans >= summ/2 :
        print(lis[i][0])
        break



