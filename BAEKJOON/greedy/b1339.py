# greedy ! 단어 수학
# 각 알파벳이 어떤 자릿수들에 등장하는지 주목

N = int(input())

digit = [0] * 26 # 알파벳 26 종류의 자릿수 합

for _ in range(N):
    num = list(input()) # 들어오는 문자열
    for i in range(len(num)-1, -1, -1): # 오른쪽부터 자릿수 따져주기
        digit[ord(num[i])-65] += 10 ** (len(num)-i-1) # 알파벳에 해당하는 digit 리스트에 자릿수 단위 넣어주기 (ex AAB면 A에 110, B에 1 넣기)
digit.sort(reverse=True) # 큰 자릿수 순으로 배열
ans = 0 # 최대 합
for i in range(10):
    ans += digit[i] * (9-i) # 자릿수 합이 큰 순으로 9~0 넣어주기
print(ans)
