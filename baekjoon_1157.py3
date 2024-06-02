word = input().upper() 
word_list = list(set(word)) 

cnt = []
for i in word_list:
    count = word.count  
    cnt.append(count(i)) 

if cnt.count(max(cnt)) > 1: #만약 최댓값이 1개 초과면
     print("?")             #? 출력

else:
    print(word_list[(cnt.index(max(cnt)))]) #아니면 가장 개수가 큰것의 문자 출력