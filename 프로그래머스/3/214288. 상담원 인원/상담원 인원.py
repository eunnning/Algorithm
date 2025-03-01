from itertools import product

def solution(k, n, reqs):
    answer = 1e9
    
    if k == 1:
        results = [(n,)]
    else:
        results = [p for p in product(range(1, n), repeat=k) if sum(p) == n]
    
    for result in results:
        
        # print(result)
        
        queues = [[] for _ in range(k)]
        
        for idx, i in enumerate(result) :
            queues[idx] = [0]*i
        
        # print(queues)
        
        tmp = 0
        for start, times, types in reqs :
            candidates = [num for num in queues[types-1] if num < start]
            if candidates:
                closest = min(candidates, key=lambda x: start - x)
            
                idx = queues[types-1].index(closest)
                queues[types-1][idx] = start + times
            else :
                closest = min((num for num in queues[types-1]), key=lambda x: x- start)
                idx = queues[types-1].index(closest)
                queues[types-1][idx] = closest + times
                tmp += (closest - start)
    
        if tmp < answer :
            answer = tmp
            
        # print(tmp)
                
    
    return answer