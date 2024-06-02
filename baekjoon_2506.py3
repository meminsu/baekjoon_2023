import sys

N = int(input())
test = list(sys.stdin.readline().split())

cnt = 0
sum = 0

for i in range(len(test)) :
    if test[i] == '1' :
        cnt += 1
        sum += cnt
    else :
        cnt = 0
print(sum)