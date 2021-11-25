# 5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# -  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних
# "х" та "у" вiдповiдь повертали рiзницю чисел.

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