while True:
  Sentence = input()
  if Sentence == '.':
    break
  else:
    stack = []
    for s in Sentence:
      if s == '(':
        stack.append('(')
      elif s == '[':
        stack.append('[')
      elif s == ')':
        if not stack or not stack.pop() == '(':
          print('no')
          break
      elif s == ']':
        if not stack or not stack.pop() == '[':
          print('no')
          break
    else:
      if stack:
        print('no')
      else:
        print('yes')
