#백준 21921 블로그
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
lis= list(map(int,input().split()))


if sum(lis) == 0 :
    print('SAD')
    exit(0)

summ = sum(lis[:m])
maxx = summ
days = 1

for i in range(m,n):
    summ += lis[i] - lis[i-m]
    if maxx == summ :
        days += 1
    elif summ > maxx :
        maxx = summ
        days = 1



print(maxx)
print(days)

