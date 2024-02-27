#백준 2660 회장뽑기
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [[1e9]*(n+1) for _ in range(n+1)]

while True:
    a,b = map(int,input().split())
    if a==-1 and b == -1 :
        break
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,n+1):
    graph[i][i] = 0


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

maxx = []

for i in range(1,n+1):
    maxx.append(max(graph[i][1:n+1]))


score = 1e9
cnt = 0
member = []

for idx, i in enumerate(maxx):
    if i < score:
        score = i
        cnt = 1
        member = [idx+1]
    elif i == score:
        cnt+=1
        member.append(idx+1)

print(score,cnt)
print(*member,end=" ")
