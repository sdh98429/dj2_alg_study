T=str(input())
numbers = T.split('-')
# print(numbers)
try:
    tot = sum(map(int,numbers[0].split('+')))
except:
    tot = 0

try:
    for number in numbers[1:]:
        tot -= sum(map(int,number.split('+')))
except:
    pass
print(tot)
