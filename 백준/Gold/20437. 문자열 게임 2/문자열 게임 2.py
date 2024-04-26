#백준 20437 문자열 게임2
import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    w = input()
    k = int(input())

    alpha = [[] for _ in range(26)]

    m = len(w)
    for i in range(m):
        word = ord(w[i]) - 97
        alpha[word].append(i)

    minn = 1e9
    maxx = -1

    for i in range(26):
        if len(alpha[i]) == k :
            # print( chr(i+97),len(alpha[i]) , alpha[i][0], alpha[i][k-1])
            maxx = max(maxx,alpha[i][k-1] - alpha[i][0] + 1)
            minn = min(minn,alpha[i][k-1] - alpha[i][0] + 1)

        elif len(alpha[i]) > k :
            for j in range(k-1, len(alpha[i])):
                # print( chr(i+97),len(alpha[i]) , alpha[i][j-k+1],alpha[i][j] )
                maxx = max(maxx,alpha[i][j] - alpha[i][j-k+1] + 1)
                minn = min(minn,alpha[i][j] - alpha[i][j-k+1] + 1)
                   

    if minn != 1e9 or maxx != -1 :
        print(minn,maxx)
    else :
        print(-1)




