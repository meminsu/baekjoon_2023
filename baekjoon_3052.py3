li = [0] * 42

for _ in range(10):
    s = int(input())
    li[s % 42] = 1 #
    
print(sum(li) )
