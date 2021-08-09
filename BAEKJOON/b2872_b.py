import sys
# 리스트 내장함수 제거, 2차 실패
T = int(input())

books = []
for i in range(1, T+1):
    books += [int(sys.stdin.readline())]

tot = 0
for act in range(T,1,-1):
    dirty = 0
    for ind in range(T):
        if books[ind] == act:
            dirty = 1
        if dirty and (books[ind] == act-1):
            books = [books[ind]] + books[:ind] +books[ind+1:]
            tot += 1

print(tot)

