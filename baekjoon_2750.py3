N = int(input())

sum_N = []
for i in range(N):
    a = int(input())
    sum_N.append(a) 
    sum_N.sort()

sum_N.sort()
for i in sum_N :
    print(i)