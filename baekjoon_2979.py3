a, b, c =map(int, input().split())

time = [0 for _ in range(100)]

for i in range(3) :
    arrive, depart = map(int, input().split())
    for j in range(arrive, depart) :
        time[j] += 1
        
total = (time.count(1) * a) + (time.count(2) * b) * 2 + (time.count(3) * c) * 3
print(total)