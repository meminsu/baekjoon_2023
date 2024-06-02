N = int(input())

answer = -1 


for five in range(N // 5*5, -1, -5): 
    left = N - five 
    if left % 3 == 0 : 
        answer = five //5 + left // 3
        break
        
print(answer)