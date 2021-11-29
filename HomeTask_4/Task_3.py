# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
# и яка вертатиме True, якщо це число просте, и False - якщо ні.

def is_prime(i):
    # while i in (0, 1, 2, 3):
    #     print('True')
    if i % 2 != 0 or i % 3 != 0:
        print('True')
    else:
        print('False')

n = int(input('Введите число для проверки: '))
is_prime(n)


