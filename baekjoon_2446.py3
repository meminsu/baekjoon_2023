n = int(input())

for i in range(0, n-1):
    print(" " * (i) + ("*") * ((n - i) * 2 - 1) )
for k in range(1, n+1):
    print(" " * (n-k) + ("*") * (k * 2 -1) )