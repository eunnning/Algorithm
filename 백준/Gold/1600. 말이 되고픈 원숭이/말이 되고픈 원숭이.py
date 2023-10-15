#백준 1600 말이 되고픈 원숭이
from collections import deque
import sys
input = sys.stdin.readline

dx_h = [-1,-2,-2,-1,1,2,2,1]
dy_h = [2,1,-1,-2,-2,-1,1,2]
dx_m = [1,-1,0,0]
dy_m = [0,0,1,-1]

k = int(input())
w,h = map(int, input().split())

lis = []

for _ in range(h) :
    lis.append(list(map(int, input().split())))



visited=[[[0]*(k+1) for _ in range(w)] for _ in range(h)]

def BFS():
    global k
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1
    while queue :
        a,b,c = queue.popleft()
        if a == h - 1 and b == w - 1 :
            return visited[a][b][c] -1
        for i in range(4):
                xx = a + dx_m[i]
                yy = b + dy_m[i]
                if xx < 0 or xx >= h or yy < 0 or yy >= w :
                    continue
                if lis[xx][yy] == 1 :
                    continue
                if visited[xx][yy][c] != 0 :
                    continue
                visited[xx][yy][c] = visited[a][b][c] + 1
                queue.append((xx,yy,c))
                
        if c < k :
            for i in range(8):
                x = a + dx_h[i]
                y = b + dy_h[i]
                if x < 0 or x >= h or y < 0 or y >= w :
                    continue
                if lis[x][y] == 1 :
                    continue
                if visited[x][y][c+1] != 0 :
                    continue
                visited[x][y][c+1] = visited[a][b][c] + 1
                queue.append((x,y,c+1))
    
    return -1


ans = BFS()
print(ans)
