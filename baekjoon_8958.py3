import sys

N = int(input())

for i in range(N) :
    A = list(sys.stdin.readline())
    len_ = len(A)
    cnt = 0
    sum = 0
    for j in range(len_) :
        if A[j] == 'O' :
            cnt +=  1
            sum += cnt
        else :
            cnt = 0
    print(sum)