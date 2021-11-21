# 8. Write a script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

pos_num = int(input('Tape a positive number: '))
n = dict()

for x in range(pos_num+1):
    n[x]= x**2
print(n)