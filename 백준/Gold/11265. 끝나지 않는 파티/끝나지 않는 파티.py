#백준 11265 끝나지 않는 파티
import sys
input = lambda: sys.stdin.readline().rstrip()
party = []
n, m = map(int, input().split())

for _ in range(n):
    party.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            party[i][j] = min(party[i][j], party[i][k]+party[k][j])
            
for _ in range(m):
    a,b,c = map(int, input().split())
    if party[a-1][b-1] <= c :
        print('Enjoy other party')
    else :
        print('Stay here')