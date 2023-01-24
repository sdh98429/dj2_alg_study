for _ in range(3):
  S = input()
  max_num = 1
  num = 1
  before = ''
  for s in S:
    if before == s:
      num += 1
      if num > max_num:
        max_num = num
    else:
      before = s
      num = 1
  print(max_num)