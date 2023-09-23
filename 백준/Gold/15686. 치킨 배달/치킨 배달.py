n,m=map(int,input().split()) #도시크기, 폐업시키지 않을 치킨집 개수
arr=[] # 도시 좌표
count=[0 for i in range(m)] # 폐업시키지 않을 치킨집 좌표
ans=1000000 # 최종 치킨 배달 거리 최솟값
for i in range(n):
    arr.append(list(map(int,input().split())))

def combination(cnt , start):
    if (cnt==m): #폐업시키지 않을 치킨집의 개수가 될 경우
        distance() #거리를 구하는 함수 실행 
        return
    for i in range(start,n*n):
        if (arr[i//n][i%n]==2): #치킨집일 경우
            count[cnt]=i #count 배열에 치킨집 좌표 저장
            combination(cnt+1,i+1) #재귀호출 i대신 start로 실행할 시 시간초과

def distance():
    summ=0
    for i in range(n*n):
        if arr[i//n][i%n]==1:
            minn=1000000 
            for x in count:
                tmp=abs(i//n-x//n)+abs(i%n-x%n) #치킨집과 집 사이의 거리 구하기
                minn=min(tmp,minn) 
            summ+=minn
    global ans
    ans=min(ans,summ)
    


combination(0,0)
print(ans)