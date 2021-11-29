# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона.

def prime_list(start, end):
    list_1 = []
    for i in range(start, end + 1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            list_1.append(i)
    return list_1

first_num = int(input('введите начальное число: \n'))
second_num = int(input('введите до какого числа получить списое: \n'))
print(prime_list(first_num, second_num))


