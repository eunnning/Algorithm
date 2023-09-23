k,n=map(int,input().split())
a=[]
res=0
maxx=0

for i in range(1,k+1):
    tmp=int(input())
    a.append(tmp)
    if tmp>maxx:
        maxx=tmp

lt=1
rt=maxx

def Count(mid):
    tmp=0
    for i in (a):
        tmp+=i//mid
    return tmp

while lt<=rt:
    mid=(lt+rt)//2
    
    if Count(mid)>=n:
        lt=mid+1
        res=mid
    else :
        rt=mid-1
print(res)