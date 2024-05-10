#백준 2467 용액
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
lis = list(map(int,input().split()))

lis.sort()

ans = []
numm = sys.maxsize

def binary(now,start,end):
    global numm, ans
    while start <= end :
        mid = (start+end)//2
        mix = lis[now] + lis[mid] 

        if abs(mix) < abs(numm):
            numm = mix
            ans = [lis[now], lis[mid]]
            
        if numm == 0 :
            return True
        if mix < 0 : 
            start = mid +1 
        else : 
            end = mid - 1 
    return False

for i in range(n-1):
    if binary(i,i+1,n-1) :
        break


print(*ans)