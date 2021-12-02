# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.


def generator_func(start: int,stop=0,step=1):
    if stop == 0:
        stop = start
        start = 0

    while start < stop:
        start += step
        yield start

    for i in generator_func(7, 3):
    print(i)

