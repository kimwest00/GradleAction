# 백준 15781 https://www.acmicpc.net/problem/15781
"""
5 7
10 60 15 20 7
1 2 3 7 5 1 3
=>67#각각 최대값 찾기
"""
def split_input():
    List = []
    List= input().split()
    List = list(map(int,List))
    return List
def find_max(num):
    weapon = split_input()
    max = weapon[0]
    for i in range(num):
        if(max < weapon[i]):
            max = weapon[i]
    return max
max_power = 0
A, B = map(int, input().split())
print(find_max(A)+find_max(B))