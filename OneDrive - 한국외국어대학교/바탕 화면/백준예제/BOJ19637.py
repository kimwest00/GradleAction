#칭호의 개수 N (1 ≤ N ≤ 105)과 칭호를 출력해야 하는 캐릭터들의 개수 M
#터 N개의 줄에 각 칭호의 이름을 나타내는 길이 1 이상, 11 이하의 영어 대문자로만 구성된 문자열과 해당 칭호의 전투력 상한값을 나타내는 109 이하의 음이 아닌 정수가 주어진다. 
#칭호는 전투력 상한값의 비내림차순으로 주어진다. 

name_num,charac_num = map(int, input().split())
name = []
name_value = []
for i in range(name_num):
    name[i],name_value[i]= input().split()
    name[i]=str(name[i])
    name_value[i]=int(name_value[i])

for i in range(charac_num):
    character[i]=int(input())
    if(character[i]<=name_value[0]):
        print("%s".format(name[i]))
    elif(name_value[1]>=character[i] >name_value[0]):
        print("")
        #name_num만큼 if문 생성<-이거 개수에따라 if문개수 출력 어떻게?!
