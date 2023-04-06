
S = input()

for s in S:
  if ord(s) - 3 < ord('A'):
    print(chr(ord(s)-3 + 26), end="")
  else:
    print(chr(ord(s)-3), end="")