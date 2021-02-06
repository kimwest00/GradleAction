initial_balance= float(input("Initial balance?\n"))#원금입력
Annual_interest_rate= float(input("Annual interest rate in percent?\n"))#년이자율 입력
print('In case initial balance is {:.2f} \nand annual interest rate is {:.2f} percent,'.format(initial_balance,Annual_interest_rate)) #입력받은 원금과 년이자율을 출력
balance = initial_balance#맨밑에 프린트되는 에서 차별성을 주기위해서 잔액을 balance 라고 이름을 설정했습니다
for i in range(20): #20회 for 루프를 돌게함
         initial=(1+rate/100.0) * initial


print('final balance after 20 years will be {:.2f}'.format(balance)) #20년후 잔고 출력
