# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий
# параметр <silent> (значення за замовчуванням - <False>).
#     Логіка наступна:якщо введено коректну пару ім'я/пароль - вертається <True>;
# якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,' \
# ' інакше (<silent> == <False>) - породжується виключення LoginException


class LoginException(Exception):
    pass
def user(username, password, silent=False):
    value_list = [username, password]
    user_list = [['Sasha', '890'], ['Rimma', '0013'], ['Dasha', '1234'], ['Igor','1111'],['Den','2345']]

    if value_list in user_list:
        return True
    if silent is True:
        return False
    raise LoginException

print(user('Sasha', '890'))