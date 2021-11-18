give = int(input('Enter a value'))
check = input('Enter a number to check the value of numbers')
g = 0
search = check.split()
for i in range(0,len(search)):
    if give == int(search[i]):
        g = 1
        break;

if g == 1:
    print('True')
else:
    print('False')