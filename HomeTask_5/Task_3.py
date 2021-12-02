# 3. На основі попередньої функції створити наступний кусок кода:
# а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції)'
#  - як валідні, так і ні;
# б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані
# і надрукує для кожної пари значень відповідне повідомлення, наприклад:
# Name: vasya
# Password: wasd
# Status: password must have at least one digit
#                                         -----
# Name: vasya
# Password: vasyapupkin2000
# Status: OK
# P.S. Не забудьте використати блок try/except ;)

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

acc_list = [['Rimma', '00130013'], ['Dennis', '12345123'],['Vasya', '11111111'], ['Sanya','fghj1234']]
for account in acc_list:
    print('Name: ', account[0])
    print('Password: ', account[1])
    print('Status: ', val_user(account[0], account[1]))