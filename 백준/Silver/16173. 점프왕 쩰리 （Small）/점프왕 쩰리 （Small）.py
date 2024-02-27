#백준 16173 점프왕젤리(small)
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

n = int(input())

lis = []

for _ in range(n):
    lis.append(list(map(int,input().split())))


def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] == 1:
        return False
    if x == n-1 and y == n-1:
        return True
    jump = lis[x][y]
    visited[x][y] = 1
    return (dfs(x+jump,y) or dfs(x,y+jump))

visited = [[0]*n for _ in range(n)]
if dfs(0,0) :
    print('HaruHaru')
else:
    print('Hing')



