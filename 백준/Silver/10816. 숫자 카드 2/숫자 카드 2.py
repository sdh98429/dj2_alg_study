import sys
input = sys.stdin.readline

def binary_search(start, end, n):
  mid = (start + end)//2
  if start > end:
    return 0
  if n == L[mid]:
    return L[start:end+1].count(n)
  elif n > L[mid]:
    return binary_search(mid+1, end, n)
  elif n < L[mid]:
    return binary_search(start, mid-1, n)
  
  

N = int(input())
L = list(map(int, input().split()))
L.sort()

card_dict = {}
for n in L:
  if n not in card_dict:
    card_dict[n] = binary_search(0, N-1, n)

M = int(input())
L_search = list(map(int, input().split()))
for l_search in L_search:
  if l_search not in card_dict:
    print(0, end=" ")
  else:
    print(card_dict[l_search], end=" ")