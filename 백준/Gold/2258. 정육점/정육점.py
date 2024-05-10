#백준 2258 정육점
import sys
input = lambda : sys.stdin.readline().strip()

n,m = map(int,input().split())
meat = []
for _ in range(n):
    w, c = map(int,input().split())
    meat.append([w,c])

meat.sort(key= lambda x :(x[1],-x[0]))

cost = []
weight = 0
samecost = 0

for i in range(n):
    w,c = meat[i]
    weight += w
    if i > 0 and c == meat[i-1][1] :
        samecost += c
    else :
        samecost = c
    if weight >= m :
        cost.append(samecost)
        if samecost == c :
            break


if cost:
    print(min(cost))
else:
    print(-1)
