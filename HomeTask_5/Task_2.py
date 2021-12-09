# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
# - щось своє :)
# Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.

class ErrorName(Exception):
    pass
class ErrorPassword(Exception):
    pass

def val_user(name, password):
    try:
        if 3 <= len(name) <= 50:
            if len(password) >= 8 and \
                    any(map(str.isdigit, password)) and \
                    any(map(str.isalpha, password)) and \
                    any(map(str.isupper, password)):
                    return True
            raise ErrorPassword
        raise ErrorName
    except ErrorName:
            print('Error: name lenght min 3 symbol, max 50 symbols')
    except ErrorPassword:
            print('PasswordError:password lenght min 8 symbols and have min one number!')

print(val_user('Rivbn', '76ASggdfgfg'))




