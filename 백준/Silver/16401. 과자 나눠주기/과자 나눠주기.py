#백준 16401 과자 나눠주기
import sys

input = sys.stdin.readline 
m, n = map(int, input().split())
lis = list(map(int,input().split()))

start = 1
end = max(lis)


while start <= end :
    mid = (start+end)//2
    tmp = 0
    for i in lis :
        tmp +=i//mid
    if tmp >= m :
        start = mid+1
    else :
        end = mid-1
            
print(end)