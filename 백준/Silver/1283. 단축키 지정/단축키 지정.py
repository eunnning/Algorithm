#백준 1283 단축키지정

import sys
input = sys.stdin.readline

n = int(input())

alphabet =[]

for i in range(n):
    word = list(input().strip())
    flag = False
    for j in range(len(word)) : # 1
        if flag == True :
            break
        if word[j] not in alphabet and (word[j-1] == ' ' or j == 0):
            alphabet.append(word[j].upper())
            alphabet.append(word[j].lower())
            word[j] = '['+word[j]+']'
            flag = True
    for j in range(len(word)): # 2
        if flag == True:
            break
        if word[j] not in alphabet and word[j] != ' ':
            alphabet.append(word[j].lower())
            alphabet.append(word[j].upper())
            word[j] = '['+word[j]+']'
            flag = True
    
    print(''.join(word))




        
        

