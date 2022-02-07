# ! 소수 찾기, permutations 사용
# 42839

from itertools import permutations # 순열 import

def prime(num): # 소수 판별
    if num <=1: # 1 이하면 return
        return 
    
    for i in range(2, int(num ** 1/2) + 1): # 제곱근까지 탐색
        if not num % i: # 나뉜다면
            return 
    else: # 끝까지 안 나뉜다면 소수
        return num

def solution(numbers):

    P = [] # 소수 종류
    for l in range(1, len(numbers)+1): # 1개부터 모든 원소 사용까지
        cand = permutations(list(numbers), l) # 모든 순열
        for can in cand:
            pri = prime(int(''.join(can))) # 현재 순열 소수 판별
            if pri and pri not in P: # 아직 없는 소수면 추가
                P.append(pri)
    return len(P)

# numbers	return
# "17"	3
# "011"	2