def solution(players, m, k):
    answer = 0
    n = len(players)
    server = [0]*24
    for i in range(n) :
        if players[i] // m > server[i] :
            tmp = players[i] // m - server[i]
            end = k+i 
            if end > 24 :
                end = 24
            for j in range(i,end) :
                server[j] += tmp
            answer += tmp
        # print(server)
                
    
    return answer