# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
# і вертатиме список простих чисел всередині цього діапазона.

import sympy

def prime_list(start, end):
    prime_list_result = [value for value in range(start, end) if sympy.isprime(value)]
    return prime_list_result


print(prime_list(1,1000))


