N = int(input())

sum = 0

for i in range(N) :
    vote = int(input())
    if vote == 1 :
        sum += 1

if sum > (N / 2) :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")