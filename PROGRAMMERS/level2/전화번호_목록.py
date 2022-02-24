# ! 전화번호 목록, 사전순 정렬
# 42577

def solution(phone_book):
    answer = True
    phone_book.sort() # 사전 순으로 정렬하면 119, 1195555, 976 순으로 정렬되어 편하다

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]): # 다음 번호보다 짧다면

            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: # 현재 번호가 다음 번호의 접두어라면
                answer = False
                break

    return answer

# phone_book	return
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false