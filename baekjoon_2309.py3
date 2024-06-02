s = []

sum = 0

for i in range(0, 9) :
    m = int(input())
    s.append(m)
    sum += m

s.sort()

ok = False

for i in range(0, 9):
    for j in range(0, 9):
        if i==j or ok == True : 
            continue 
        if sum-(s[i]+s[j]) == 100:
            ok = True 
            for k in range(0, 9) :
                if k == i or k == j :
                    continue 
                print(s[k])