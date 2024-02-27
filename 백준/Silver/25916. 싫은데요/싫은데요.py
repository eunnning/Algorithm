#백준 25916 싫은데요
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
lis= list(map(int,input().split()))

start = 0
end = 0
tmp = 0
ans = 0
while end < n:
    if lis[end] + tmp <= m :
        tmp += lis[end]
        ans = max(ans,tmp)
        end +=1
    else :
        tmp += lis[end] 
        end += 1
        while tmp > m :
            tmp -= lis[start]
            start += 1
        ans = max(ans,tmp)


print(ans)
