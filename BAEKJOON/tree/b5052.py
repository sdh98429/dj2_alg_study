# tree !! 전화번호 목록
# 요번엔 다른 사람 코드도 좀 참고함
# 문자열인 상태로 sort하면 알파벳 순 정렬되어 도서관 책 목록처럼 '123' '1235' '125' 순으로 배열됨
# 길이 같은 상태면 일관성 다를리 없으니 넘기고
# 길이 다른 상태면 더 짧은 길이로 일일히 비교

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    book = []
    for _ in range(N):
        book.append(input())
    book.sort() # 알파벳 순 정렬

    flag = False # 일관성 flag
    for i in range(N-1):
        if len(book[i]) == len(book[i+1]): # 길이 같으면 일관성 다를 수 없음
            continue

        min_num = min(len(book[i]), len(book[i+1]))
        for j in range(min_num):
            if book[i][j] != book[i+1][j]: # 더 짧은 길이로 비교
                break
        else:
            flag = True
            break


    if flag:
        print('NO')
    else:
        print('YES')