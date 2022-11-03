L = int(input())
S = input()
hash = 0
for i in range(len(S)):
  hash += (ord(S[i])-96) * 31 ** i
print(hash%1234567891)
