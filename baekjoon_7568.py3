N = int(input())
cnt_list = []
bbig = []

for _ in range(N) :
    num = list(map(int, input().split() ) )
    bbig.append(num)
    
for i in range(N):
    cnt = 0
    for j in range(N) :
        if bbig[i][0] < bbig[j][0] and bbig[i][1] < bbig[j][1] :
            cnt += 1
    cnt_list.append(cnt+1)

print(*cnt_list)
    