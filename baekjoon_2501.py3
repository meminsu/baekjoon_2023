import sys
N, K = map(int, sys.stdin.readline().split())
num = []

for i in range(1, N+1) :
    if N % i == 0 :
        num.append(i)

if len(num) < K :
    print(0)
else:
    print(num[K-1])