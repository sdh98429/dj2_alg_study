L = list(map(int, input().split()))
if L == [i for i in range(1, 9)]:
    print('ascending')
elif L == [i for i in range(8, 0, -1)]:
    print('descending')
else:
    print('mixed')