import sys
input = sys.stdin.readline

N = int(input())

L = [input().split() for _ in range(N)]

for tc in range(1, N+1):
    word = ''
    print('Case #{}: '.format(tc), end='')
    for l in L[tc-1][::-1]:
        print(l, end=' ')
    print(word)