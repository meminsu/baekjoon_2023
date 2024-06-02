E,S,M,cnt =1,1,1,1

r_E , r_S , r_M = map(int,input().split() )

while(True):
    if r_E == E and r_S == S and r_M == M :
        break
    E += 1 ; S += 1 ; M += 1; cnt += 1
    if E >= 16 : E -= 15
    if S >= 29 : S -= 28
    if M >= 20 : M -= 19
        
print(cnt)