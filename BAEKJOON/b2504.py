# (()[[]])([])
# [][]((])
# []]
# (((()
from collections import deque

bracket = list(input())

def check(bra):
    for b in bra:
        # print(stack)
        if not stack:
            if b == ')' or b == ']':
                return 0
            else:
                stack.append(b)
        else:
            if b == ')':
                n = stack.pop()
                plus = flag = 0
                while n != '(':
                    if n == '[':
                        return 0
                    else:
                        flag = 1
                        plus += n
                    if stack:
                        n =stack.pop()
                    else: # []] 3]
                        return 0
                else:
                    if not flag:
                        stack.append(2)
                    else:
                        stack.append(plus*2)

            elif b == ']':
                n = stack.pop()
                plus = flag = 0
                while n != '[':
                    if n == '(':
                        return 0
                    else:
                        flag = 1
                        plus += n
                    if stack:
                        n =stack.pop()
                    else:
                        return 0
                else:
                    if not flag:
                        stack.append(3)
                    else:
                        stack.append(plus*3)

            else:
                stack.append(b)
                

    else:
        try:
            return sum(stack) # (((()
        except: 
            return 0


stack = deque([])
print(check(bracket))