# 2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі
# < a > одиниць строком на < years > років під < percents > відсотків (кожен рік сума вкладу збільшується на цей
# відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). Функція повинна' \
# принтануть і вернуть суму, яка буде на рахунку.


def bank(money, years, percent=10):
    for year in range(years):
        money = money*(percent/100)+money
    return "%.2f" % money
money=int(input('Введите сумму вклада: '))
years=int(input('Введите на сколько лет: '))
# percent=int(input('Введите процент: '))
print(bank(money, years, percent=10))