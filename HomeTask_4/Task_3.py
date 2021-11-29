# 3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
# и яка вертатиме True, якщо це число просте, и False - якщо ні.

def is_prime(k):
    k = 0
    for i in range(2, n// 2+1):
        if (n % i ==0):
            k = k + 1
    if (k <=0):
        print('True')
    else:
        print('False')

n = int(input('Введите число для проверки: '))
is_prime(n)


