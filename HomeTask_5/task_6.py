# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.

class RangeException(Exception):
    pass

def gen_func(start:int, stop=0, step=1):
    if start == stop +1:
        yield []
    else:
        if start == stop:
            raise RangeException
        else:
            if step == 0:
                raise RangeException
            if step > 0:
                if stop == 0:
                    stop = start
                    start = 0
                while start < stop:
                    yield start
                    start += step
            if step < 0:
                if stop == 0:
                    stop = start
                    start = 0
                while start > stop:
                    yield start
                    start += step

for i in gen_func(0,10):
    print(i)