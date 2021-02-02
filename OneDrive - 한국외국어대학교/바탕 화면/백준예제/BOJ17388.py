participate = input.split()
#participate는 숭,고,한의 참여도를 담은 리스트
if(participate[0]+participate[1]+participate[2]>=100):
    print("OK")
else:
    if(participate[0]<participate[1] and participate[0]<participate[2]):
        print("Soongsil")
    else if(participate[1]<participate[0] and participate[1]<participate[2]):
        print("Korea")
    else if(participate[2]<participate[0] and participate[2]<participate[1]):
        print("Hanyang")