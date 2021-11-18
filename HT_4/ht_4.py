n = int(input('Enter a number of concatenation string: '))

con_string = ''

for i in range(n):
    myStr = input('Enter a string to concanate: ')
    con_string += myStr

print('Result: ',con_string)
