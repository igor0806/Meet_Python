# 1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
# і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.

def square(kvadrat):

    return (4 * kvadrat, kvadrat * 2, (2 * kvadrat * 2)**.5)

result = square(int(input('Введите сторону квадрата: ')))
print(result)