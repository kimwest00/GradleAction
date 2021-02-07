score =[]
for i in range(5):
    cook_score= map(int,input().split())
    for j in range(4):
        score[i] += cook_score[j]#indexerror_map은 index를 사용할수없다!
max = score[0]
max_num = 0
for i in range(5):
    if(max<score[i]):
        max = score[i]
        max_num = i
print("%d %d".format(max_num,max))