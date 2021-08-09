import sys
# 리스트 내장 함수 시도, 1차 실패
T = int(input())

# books = []
# for tc in range(1, T+1):
#     book = int(input())
#     books.append(book)
books =[int(sys.stdin.readline())]

for i in range(1,T):
    books.append(int(sys.stdin.readline()))

tot = 0
for act in range(T,1,-1):
    if books.index(act) < books.index(act - 1):
        books.pop(books.index(act - 1))
        books.insert(0, act - 1)
        tot += 1
print(tot)

