# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя

def some_func(something):
    if 30 < len(something) < 50:
        print(len(something))
        print(len([x for x in something if x.isalpha()]))
        print(len([x for x in something if x.isnumeric()]))

    if len(something) < 30:
        print(sum([int(x) for x in something if x.isnumeric()]))

    if len(something) > 50:
        print(sorted(something))

print(some_func(input()))