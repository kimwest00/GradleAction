initial_balance= float(input("Initial balance?\n"))#원금입력
Annual_interest_rate= float(input("Annual interest rate in percent?\n"))#년이자율 입력
print('In case initial balance is {:.2f} \nand annual interest rate is {:.2f} percent,'.format(initial_balance,Annual_interest_rate)) #입력받은 원금과 년이자율을 출력
balance = initial_balance#맨밑에 프린트되는 에서 차별성을 주기위해서 잔액을 balance 라고 이름을 설정했습니다
balance= float(balance* ((Annual_interest_rate/100) +1))#1년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#2년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#3년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#4년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#5년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#6년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#7년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#8년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#9년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#10년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#11년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#12년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#13년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#14년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#15년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#16년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#17년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#18년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#19년후 잔액
balance= float(balance* ((Annual_interest_rate/100) +1))#20년후 잔액





print('final balance after 20 years will be {:.2f}'.format(balance)) #20년후 잔고 출력
