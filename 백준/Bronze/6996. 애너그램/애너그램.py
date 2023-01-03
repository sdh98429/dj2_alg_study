T = int(input())

for tc in range(T):
  A, B = input().split()
  a = sorted(list(A))
  b = sorted(list(B))

  if a==b:
    print(A, "&", B, "are anagrams.")
  else:
    print(A, "&", B, "are NOT anagrams.")