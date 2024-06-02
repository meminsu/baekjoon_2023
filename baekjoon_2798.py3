N, M = map(int, input().split() )
card = list(map(int, input().split() ) )

result = list()

for i in range(N): 
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if (M >= (card[i] + card[j] + card[k])):
                result.append(card[i] + card[j] + card[k])
                
print(max(result))