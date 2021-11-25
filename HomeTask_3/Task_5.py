def numbers(x, y):
    if x > y or x < y:
        result = abs(x - y)
        if x > y:
            return f'{x} more than {y} by {result}'
        else:
            return f'{y} more than {x} by {result}'
    elif x == y:
            result = x
            return f'{x} equal {result}'
first_num = float(input('Insert first number'))
second_num = float(input('Insert second number'))
print(numbers(first_num, second_num))