# 5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі,
# що не перевищують його.

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        if b<=n:
            print(b, end='')
            a, b = b, a + b


num = fibonacci(int(input('Введите число: ')))
