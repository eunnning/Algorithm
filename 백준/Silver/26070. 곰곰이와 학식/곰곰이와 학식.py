#백준 26070 곰곰이와 학식
import sys
input = lambda: sys.stdin.readline().rstrip()

a,b,c = map(int,input().split())
x,y,z = map(int,input().split())

cnt = 0

if a >= x :
    cnt += x
    a -= x
    x = 0
else : 
    cnt += a
    x -= a
    a = 0
if b >= y :
    cnt += y
    b -= y
    y = 0
else : 
    cnt += b
    y -= b
    b = 0
if c >= z :
    cnt += z
    c -= z
    z = 0
else : 
    cnt += c
    z -= c
    c = 0


while True:
    if x // 3 == 0 and y // 3 == 0 and z //3 == 0 :
        break
    if a == b == c == 0:
        break
    if x > 0 :
        y += x//3
        x %= 3
        if b >= y :
            cnt += y
            b -= y
            y = 0
        else : 
            cnt += b
            y -= b
            b = 0
    if y > 0 :
        z += y//3
        y %= 3
        if c >= z :
            cnt += z
            c -= z
            z = 0
        else : 
            cnt += c
            z -= c
            c = 0
    if z > 0:
        x += z//3
        z %= 3
        if a >= x :
            cnt += x
            a -= x
            x = 0
        else : 
            cnt += a
            x -= a
            a = 0

print(cnt)

    

