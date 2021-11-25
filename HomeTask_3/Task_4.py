# 4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат.
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def function_1(function):
    return function

def function_2():
    return 'And i am'

def function_3():
    return 'SUPERSTAR '

def function_4():

    my_text = 'Hi I am 40'

    result = function_1(my_text), function_2(), function_3()

    return result

print(function_4())