#백준 1011 Fly me to the Alpha Centauri
import math
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x,y = map(int, input().split())
    diff = y - x
    if diff == 1 :
        print(1)
    elif diff == 2 :
        print(2)
    elif diff == 3 :
        print(3)
    else :
        n = int(math.sqrt(diff)) 
        cnt = n * 2 - 1
        ans = diff - n*n
        if ans != 0 :
            if ans <= n :
                cnt +=1
            else :
                cnt +=2
        print(cnt)
        



