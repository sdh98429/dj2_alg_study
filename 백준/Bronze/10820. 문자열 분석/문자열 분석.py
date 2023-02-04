

while True:
  try:
    S = input()
    low, up, num, space = 0, 0, 0, 0
    for s in S:
      if s.islower():
        low += 1
      elif s.isupper():
        up += 1
      else:
        try:
          int(s)
          num += 1
        except:
          space += 1
    print(low, up, num, space)
  except EOFError:
    break