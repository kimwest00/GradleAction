number = int(input())
'''
빼먹은 조건
1.0은 지울게 있다는 가정하에 문제에서 사용_리스트를 0으로 초기화하거나, remove함수를 안쓸이유가 없음
2.0은 "가장 최근에남아있는 원소"를 지우는 역활을 한다
'''
score_list= []#else:에서 가장 마지막줄에 있는 원소를 0으로 치환해야하는데 

total_score = 0
for i in range(number):
    score= int(input())
    if(score !=0):
        score_list.append(score)
    else:
        score_list.remove(score_list[-1])
        
for i in score_list:
    total_score += i
    
print(total_score)