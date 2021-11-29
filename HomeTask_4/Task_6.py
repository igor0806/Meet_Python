# 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100,' \
# якщо дорівнює 0, не змінювати.

def numbers(n):
    if n > 0:
        n = (n **2)
        return n
    elif n < 0:
        n =  (n + 100)
        return n
    elif n == 0:
        return 0

result = numbers(int(input('введите число: ')))
print(result)





