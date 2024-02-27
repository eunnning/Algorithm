#백준 17352 여러분의 다리가 되어 드리겠습니다
import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b :
        return 
    parent[b] = a
    
n = int(input())
graph = []
parent = [ i for i in range(n+1)]

for _ in range(n-2):
    a,b = map(int,input().split())
    union(a,b)


ans =[]
for i in range(1,n+1):
    if i == parent[i]:
        ans.append(i)

print(*ans)