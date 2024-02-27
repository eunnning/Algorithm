#백준 24460 특별상이라도 받고 싶어
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

n = int(input())

lis = []

for _ in range(n):
    lis.append(list(map(int,input().split())))

def recursive(x,y,size):
    if size == 1 :
        return lis[x][y]
    else :
        tmp = [recursive(x,y,size//2),recursive(x+size//2,y,size//2),recursive(x,y+size//2,size//2),recursive(x+size//2,y+size//2,size//2)]
        tmp.sort()
        return tmp[1]


print(recursive(0,0,n))
