n = int(input())
n_1 = list(map(int, input().split() ) )
v = int(input())

result = 0
for i in range(n) :
    if n_1[i] == v :
        result += 1
print(result)
