# 백준 10026 적록색약

from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())
lis = []
visited_y =[[False]*n for _ in range(n)]
visited_n =[[False]*n for _ in range(n)]

color_y = 0
color_n = 0


for i in range(n):
    lis.append(list(input().strip()))

lis_n = copy.deepcopy(lis)

for i in range(n):
    for j in range(n):
        if lis_n[i][j]=='G':
            lis_n[i][j]='R'


def bfs_y (x, y):
    queue = deque([(x,y)])
    visited_y[x][y]= True
    color = lis[x][y]
    
    while queue :
        a,b = queue.popleft()
        for k in range(4):
            i = a+dx[k]
            j = b+dy[k]
            if ( i>=0 and j>= 0 and i<n and j<n):
                if (lis[i][j] == color and not visited_y[i][j] ):
                    visited_y[i][j]=True
                    queue.append([i,j])
def area_y():
    global color_y
    for i in range(n):
        for j in range(n):
            if not visited_y[i][j] :
                color_y +=1
                bfs_y(i,j)
    
def bfs_n (x, y):
    queue = deque([(x,y)])
    visited_n[x][y]= True
    color = lis_n[x][y]
    
    while queue :
        a,b = queue.popleft()
        for k in range(4):
            i = a+dx[k]
            j = b+dy[k]
            if ( i>=0 and j>= 0 and i<n and j<n):
                if (lis_n[i][j] == color and not visited_n[i][j] ):
                    visited_n[i][j]=True
                    queue.append([i,j])
def area_n():
    global color_n
    for i in range(n):
        for j in range(n):
            if not visited_n[i][j] :
                color_n +=1
                bfs_n(i,j)
    


area_y()
area_n()

print(color_y,color_n)