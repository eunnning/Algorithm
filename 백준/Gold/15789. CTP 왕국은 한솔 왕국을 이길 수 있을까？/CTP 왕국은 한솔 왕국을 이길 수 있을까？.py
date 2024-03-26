#백준 15789 CTP 왕국은 한솔 왕국을 이길 수 있을까
import sys
input = lambda: sys.stdin.readline().rstrip()

def union(x,y):
    a = find(x)
    b = find(y)
    if group[a] >= group[b]:
        parent[b] = a
        group[a] += group[b]
    else :
        parent[a] = b
        group[b] += group[a]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def is_root(x):
    return parent[x] == x

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
group = [1 for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    if find(x) != find(y):
        union(x,y)

c,h,k = map(int, input().split())

ans = []
C = find(c)
H = find(h)
answer = group[C]

visited =[0]*(n+1)
visited[C] = 1

for i in range(1,n+1):
    I = find(i)
    if I == H or I == C or visited[I]:
        continue
    ans.append(group[I])
    visited[I] = 1

ans.sort(reverse=True)

if k >= len(ans) :
    answer += sum(ans)
else :
    for i in range(k):
        answer += ans[i]

print(answer)