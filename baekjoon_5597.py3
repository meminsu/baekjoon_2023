class_ = [i for i in range(1,31)] 

for i in range(28) :
  num = int(input()) 
  class_.remove(num)

print(*class_, sep ="\n")