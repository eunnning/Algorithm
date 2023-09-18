import sys
input = sys.stdin.readline
n = int(input()) #행성의 개수
parent = [i for i in range(n)] 
x = []
y = []
z = []

# 각 행성번호를 함께 저장
for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

# 특정 원소가 속한 집합을 찾기
def find(x):
    if parent[x] == x:
        return x
    else: 
        parent[x] = find(parent[x])
        return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

## 거리 계산, (행성 사이 거리, 행성1, 행성2) 정보 저장 
dist = []
for i in range(n-1):
    dist.append((x[i+1][0] - x[i][0], x[i+1][1], x[i][1]))
    dist.append((y[i+1][0] - y[i][0], y[i+1][1], y[i][1]))
    dist.append((z[i+1][0] - z[i][0], z[i+1][1], z[i][1]))

ans = 0
dist.sort()

for cost, i, j in dist:
    if find(i) != find(j):
        union(i, j)
        ans += cost

print(ans)
