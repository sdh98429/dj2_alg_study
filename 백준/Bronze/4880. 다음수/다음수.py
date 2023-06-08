while True:
  A, B, C = map(int, input().split())
  if A or B or C:
    if B - A == C - B:
      print('AP', 2 * C - B)
    else:
      print('GP', int(C * (C/B)))

  else:
    break