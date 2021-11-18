value_a = int(input('Enter a value a: '))
value_b = int(input('Enter a value b: '))
search = input('Enter a number to check the value of numbers')
search_list = search.split(',')
g = []

for i in search_list:
    g.append(int(i))
if value_a in g:
    print('True')
else:
    print('False')
if value_b in g:
    print('True')
else:
    print('False')