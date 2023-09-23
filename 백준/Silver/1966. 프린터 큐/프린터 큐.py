#백준 1966 프린터 큐
from collections import deque

T = int(input())

for i in range(T):
    N,M = map(int, input().split()) # n : 문서의 개수, m : 궁금한 문서가 몇번째에 놓여져 있는지
    cnt = 0
    lis = list(map(int, input().split()))
    q = deque()

    for idx, a in enumerate(lis) :
        q.append((a,idx))

    maxx = max(lis)

    while len(q) != 0 :
        a,idx = q.popleft()
        if a == maxx:
            cnt+=1
            if idx == M :
                print(cnt)
                break
            lis.remove(maxx)
            maxx = max(lis)
        else :
            q.append((a,idx))
            




