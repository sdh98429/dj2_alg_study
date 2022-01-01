# queue ! 큐 2
# 큐 empty 조건 언제나 확인하고 시작하기
import sys

N = int(input())
Q = [-1] * (N+1)
front = -1
rear = -1

for _ in range(N):
    com = sys.stdin.readline().split()
    if len(com) == 2: # push로 입력
        rear += 1
        Q[rear] = com[1]
    else: # pop으로 입력
        if com[0] == 'pop':
            if front != rear:
                front += 1
                print(Q[front])
            else:
                print(-1)
        elif com[0] == 'size':
            print(rear - front)
        elif com[0] == 'empty':
            print(1) if front == rear else print(0)
        elif com[0] == 'front':
            if front == rear:
                print(-1)
            else:
                print(Q[front+1])
        elif com[0] == 'back':
            if front == rear:
                print(-1)
            else:
                print(Q[rear])