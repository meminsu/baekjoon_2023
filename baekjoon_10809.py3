S = input() 
abc ='abcdefghijklmnopqrstuvwxyz' 

for i in abc: 
    if i in S: 
        print(S.index(i), end= ' ') #알파벳의 순서대로 한개씩 S에 있는 단어의 인덱스 값을 출력
    else:
        print( -1, end =' ') #S에 특정 알파벳이 없다면 -1 출력