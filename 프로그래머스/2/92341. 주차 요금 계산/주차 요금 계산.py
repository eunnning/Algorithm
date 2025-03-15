import math
def solution(fees, records):
    answer = []
    
    newRecords = []
    for record in records:
        newRecords.append(record.split())
    
    newRecords.sort(key=lambda x:x[1])
    
    while newRecords:
        nowCarNum = newRecords[0][1]
        car = []
        while newRecords and nowCarNum == newRecords[0][1]:  
            car.append([newRecords[0][0], newRecords[0][2]])
            del newRecords[0]
        
        if len(car) % 2 == 1 :
            car.append(["23:59", "OUT"])
        
        hOut = sum([int(x[0].split(':')[0])  for x in car if x[1]=='OUT'])
        hIn = sum([int(x[0].split(':')[0])  for x in car if x[1]=='IN'])
        mOut = sum([int(x[0].split(':')[1])  for x in car if x[1]=='OUT'])
        mIn = sum([int(x[0].split(':')[1])  for x in car if x[1]=='IN'])
        
        time = (hOut-hIn)*60 + (mOut-mIn)
        
        if time < fees[0] :
            fee = fees[1] 
        else :
            fee = fees[1] + math.ceil((time - fees[0])/fees[2])*fees[3]
        
        answer.append(fee)
                        
    
    
    
    return answer