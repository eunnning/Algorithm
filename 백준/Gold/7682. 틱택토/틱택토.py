#백준 7682 틱택토
import sys
iuput = lambda : sys.stdin.readline().strip()

while True :
    tictakto = list(input().strip())
    if tictakto == ['e','n','d']:
        break

    # 서로 번갈아 가며 말을 놓는지 확인
    xc = tictakto.count('X')
    oc = tictakto.count('O')
    if not ((xc == oc+1) or (xc == oc)) :
        print('invalid')
        continue

    # 성공했는지 확인
    oresult = False
    xresult = False
    if (tictakto[0] == tictakto[1] == tictakto[2] ) and tictakto[0] == 'X' :
        xresult = True
    elif (tictakto[0] == tictakto[1] == tictakto[2] ) and tictakto[0] == 'O' :
        oresult = True
   
    if (tictakto[0] == tictakto[3] == tictakto[6]) and tictakto[0] == 'X' :
        xresult = True
    elif (tictakto[0] == tictakto[3] == tictakto[6]) and tictakto[0] == 'O' :
        oresult = True

    if (tictakto[0] == tictakto[4] == tictakto[8] )and tictakto[0] == 'X' :
        xresult = True
    elif (tictakto[0] == tictakto[4] == tictakto[8] ) and tictakto[0] == 'O' :
        oresult = True
    
    if (tictakto[3] == tictakto[4] == tictakto[5] )and tictakto[3] == 'X' :
        xresult = True
    elif (tictakto[3] == tictakto[4] == tictakto[5] )and tictakto[3] == 'O':
        oresult = True

    if (tictakto[1] == tictakto[4] == tictakto[7] )and tictakto[1] == 'X' :
        xresult = True
    elif (tictakto[1] == tictakto[4] == tictakto[7] )and tictakto[1] == 'O' :
        oresult = True


    if (tictakto[2] == tictakto[4] == tictakto[6] )and tictakto[2] == 'X' :
        xresult = True
    elif (tictakto[2] == tictakto[4] == tictakto[6] )and tictakto[2]  == 'O':
        oresult = True

    if (tictakto[6] == tictakto[7] == tictakto[8]) and tictakto[6] == 'X':
        xresult = True
    elif (tictakto[6] == tictakto[7] == tictakto[8]) and tictakto[6] == 'O' :
        oresult = True

    if (tictakto[2] == tictakto[5] == tictakto[8] )and tictakto[2]  == 'X' :
        xresult = True
    elif (tictakto[2] == tictakto[5] == tictakto[8] )and tictakto[2]   == 'O':
        oresult = True
    
    # 둘다 성공함 
    if xresult and oresult :
        print('invalid')
        continue
    # 누군가가 이기지 않았지만 게임판이 가득참
    if not xresult and not oresult and tictakto.count('.') == 0 :
        print('valid')
        continue
    # X 성공
    if xresult and not oresult and xc > oc :
        print('valid')
        continue
    # O 성공
    if not xresult and oresult and xc == oc :
        print('valid')
        continue


    # 이기지도 않고 게임판이 가득차지도 않음
    print('invalid')

