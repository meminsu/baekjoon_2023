bird = int(input())

cnt = 0
time = 0

while bird != 0 :
    if bird > cnt :
        cnt +=1
        time +=1
        bird -= cnt
        if cnt >= bird :
            cnt = 0
    else :
        bird = 0
        
print(time)