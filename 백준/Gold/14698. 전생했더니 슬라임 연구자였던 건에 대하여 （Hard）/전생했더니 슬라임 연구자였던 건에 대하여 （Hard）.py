#백준 14698 전생했더니 슬라임 연구자였던 건에 대하여(Hard)
import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    slime = list(map(int, input().split()))
    
    heapq.heapify(slime) 
        
    result = 1
    
    while len(slime) > 1 :
        n1 = heapq.heappop(slime)  
        n2 = heapq.heappop(slime)
        num = (n1% 1000000007) * (n2 % 1000000007)
        heapq.heappush(slime,num)
        result = (result * num) %1000000007

    print(result)

