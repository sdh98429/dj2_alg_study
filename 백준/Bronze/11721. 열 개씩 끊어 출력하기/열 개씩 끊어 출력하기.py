S = list(input())

for i in range(((len(S)-1)//10)+1):
    try:
        print(''.join(S[10*i:10*(i+1)]))
    except:
        print(''.join(S[10*i:]))