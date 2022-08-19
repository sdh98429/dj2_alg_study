while True:
  A, B = map(int, input().split())
  if A or B:
    if not A%B:
      print('multiple')
    elif not B%A:
      print('factor')
    else:
      print('neither')
  else: 
    break