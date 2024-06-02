n = int(input())

for i in range(1, n):
    print("*" * i + " " * ((n-i)*2) + "*" * (i))
for k in range(0, n) :
    print("*" * (n-k) + " " * (k * 2)  + "*" * (n-k))