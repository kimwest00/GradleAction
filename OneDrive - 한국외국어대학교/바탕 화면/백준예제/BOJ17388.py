#participate 변수를 한꺼번에 int로 못바꾸냐,,
participate = input().split()#AttributeError: 'builtin_function_or_method' object has no attribute 'split'  나니까 괄호쓰라고 야발^^
participate[0]=int(participate[0])
participate[1]=int(participate[1])
participate[2]=int(participate[2])
if(participate[0]+participate[1]+participate[2]>=100):
    print("OK")
else:
    if(participate[0]<participate[1] and participate[0]<participate[2]):
        print("Soongsil")
    elif(participate[1]<participate[0] and participate[1]<participate[2]):
        print("Korea")
    elif(participate[2]<participate[0] and participate[2]<participate[1]):
        print("Hanyang")
    #elif -> 파이썬 else if->c언어...민하다 추서야