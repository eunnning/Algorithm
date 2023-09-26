n, m = map(int, input().split())
lis = list(map(int,input().split()))

lis.sort()

start=0
end=max(lis)
result=200000000
while start <= end:
    summ=0
    mid=(start+end)//2
    for x in lis:
        if mid < x:
            summ+= x-mid
    
    if summ>= m:
        result=min(result,summ)
        start= mid+1
    else :
        end=mid-1

print(end)
