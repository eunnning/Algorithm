#백준 1105 팔
import sys
input = sys.stdin.readline

l, r = map(int, input().split())

l =list(map(int, str(l)))
r =list(map(int, str(r)))

count = 0
if len(l) != len(r):
    pass
else :
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == 8:
                count +=1
        else :
            break

print(count)
