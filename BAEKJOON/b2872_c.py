import sys
# 4 2 3 1 4 일떄 오류, 3차 실패
T = int(input())

books = []
for i in range(1, T+1):
    books += [int(sys.stdin.readline())]

tot = 0
while True:
    for act in range(T-1):
        if books[act] > books[act+1]:
            books = [books[act+1]] + books[:act+1] + books[act+2:]
            tot += 1
            break
    else:
         break
        
print(tot)

