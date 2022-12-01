S = input()
for s in S:
  if 97 <= ord(s) and ord(s) <= 122:
    if ord(s) +13 >122:
      print(chr((ord(s)+13)%123 +97), end="")
    else:
      print(chr((ord(s)+13)), end="")
  elif 65 <= ord(s) and ord(s) <= 90:
    if ord(s) +13 > 90:
    # print((ord(s)+13)%91 +65)
      print(chr((ord(s)+13)%91 +65), end="")
    else:
      print(chr((ord(s)+13)), end="")
  else:
    print(s, end="")
