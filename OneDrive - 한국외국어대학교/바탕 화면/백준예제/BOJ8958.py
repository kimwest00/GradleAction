# 백준 8958 https://www.acmicpc.net/problem/8958
'''
5
OOXXOXXOOO                10(1+2+1+1+2+3)
OOXXOOXXOO                9 (1+2+1+2+1+2)
OXOXOXOXOXOXOX             7
OOOOOOOOOO                 55
OOOOXOOOOXOOOOX            30
'''
N = int(input())
for i in range(N):
    score = 0
    stack = 0
    text = input()
    for j in text:#text[j]로 하면 TypeError: string indices must be integers
        if(j=='O'):
            score += 1
            score += stack
            stack += 1
        else:
            stack = 0
    print(score)
