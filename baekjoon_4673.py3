num = set(range(1, 10001))
self_num = set()

for i in num :
    for j in str(i) :
        i += int(j)
    self_num.add(i)

self_num_st = sorted(num - self_num)

for num in self_num_st:
  print(num)