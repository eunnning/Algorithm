#백준 1043 거짓말
import sys
iuput = lambda : sys.stdin.readline().strip()

n,m = map(int,input().split())
truth = list(map(int,input().split()))
del truth[0]

truth = set(truth)

party = []
for _ in range(m):
    tmp = list(map(int,input().split()))
    del tmp[0]
    party.append(tmp)

now = len(truth)
next = 0
while True : 
    for case in party :
        case = set(case)
        if len(case & truth) > 0 :
            truth.update(case)
    next = len(truth)
    if now == next :
        break
    now = next


cnt = 0
for case in party :
    case = set(case)
    if len(case & truth) == 0 :
        cnt += 1
        
print(cnt)

