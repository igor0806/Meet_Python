# 8.Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
# Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок,
# якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).

def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
        return lst
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
        return lst

nums = [4, 5, 6, 7, 8, 9, 0]
result = shift(nums,int(input('введите число: ')))
print(result)


