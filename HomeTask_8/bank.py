import json
from pathlib import Path
import banknotes

def start():
    def user_valid():
        for n in data:
            if n['name'] == name and n['password'] == password:
                menu()
                usr_type = ''.join([n["type"] for n in data if n['name'] == name])
                return
        raise PermissionError('Пароль или имя неверны')

    def menu():
        while True:
            menu_user = '1 Посмотреть баланс\n' \
                        '2.Пополнить счет\n' \
                        '3.Снять со счета\n' \
                        '4.Выход'
            incasator = '1.Посмотреть купюры в наличии\n' \
                        '2.Добавить купюры\n' \
                        '3.Выход'

            if usr_type == 'incasator':
                print(incasator)
                choice = input("Введите действие: ")
                while True:

                    if choice == '1':
                        incasator_function(False)
                        break
                    if choice == '2':
                        incasator_function(True)
                        break
                    if choice == '3':
                        start()
                    else:
                        print(f"Вы ввели неправильно действие")
                        break
            elif usr_type == 'user':
                print(menu_user)
                choice = input("Введите действие: ")
                while True:
                    if choice == '1':
                        print("Ваш баланс: ", balance()[0].get('balance'))
                        break
                    if choice == '2':
                        f_money = input("Введите сумму пополнения: ")
                        if not f_money.isdigit():
                            print("Ви ввели не правильно действие, попробуйте еще раз")
                            break

                        add_money(int(f_money))
                        break
                    if choice == '3':
                        g_money = input("Введите сумму для снятия: ")
                        if not g_money.isdigit():
                            print("Ви ввели не правильно действие, попробуйте еще раз")
                            break

                        give_money(int(g_money))
                        break
                    if choice == '4':
                        start()
                    else:
                        print(f"Ви ввели не правильно действие, попробуйте еще раз")
                        break
    def balance():
        with open(outpath / "balance" /f'{name}_balance.json', "r+") as file:
            data_file = json.load(file)
            return data_file

    def give_money(g_money):
        initial_balance = balance()[0].get('balance')
        balance_now = balance()
        if g_money > balance_now[0]['balance'] or g_money < 0:
            return
            print("Недостаточно денег на счету")
        banknotes.start_banknotes(g_money)

        balance_now[0]['balance'] = balance()[0].get('balance') - g_money
        print('Ваш баланс: ', balance_now[0]['balance'])

        with open(outpath / "balance" / f'{name}_balance.json', "w") as file:
            json.dump(balance_now, file)
        trans(give_money.__name__, initial_balance, g_money)

    def add_money(f_money):

        initial_balance = balance()[0].get('balance')
        balance_now = balance()

        balance_now[0]['balance'] = balance()[0].get('balance') + f_money
        print('Ваш баланс: ', balance_now[0]['balance'])
        with open(outpath / "balance" /f'{name}_balance.json', "w") as file:
            json.dump(balance_now,file)
        trans(add_money.__name__, initial_balance, f_money)


    def trans(name_trans,balance_before,sum_trans):



        data = {'Name': name,
                'type_user': usr_type,
                'transaction': name_trans,
                'balance before ': balance_before,
                'sum of trans': sum_trans,
                'balance after': balance()[0].get('balance'),

                }

        with open(outpath / "transactions" / f'{name}_transactions.json', "r+") as file:
            read_t = json.load(file)
            read_t.append(data)
        with open(outpath / "transactions" / f'{name}_transactions.json', "w") as file2:
            file2.write('[')
            for i in read_t:
                json.dump(i, file2)
                if i != read_t[-1]:
                    file2.write(', \n')
            file2.write(']')



    def incasator_function(action):
        with open("bank_money.json.json", "r+") as file:
            data_incasator = json.load(file)
            if not action:
                for i in data_incasator:
                    print(i)
            elif action:
                banknote = input("Введите номинал купюры: ")
                check = False
                num_banknote = input("Введите количество купюр: ")
                if not num_banknote.isdigit():
                    return
                    print('Вы ввели неправильное число')
                print(data_incasator)
                for i in data_incasator:
                    if banknote in i:
                        i[banknote] = int(num_banknote)
                        check = True
                print(data_incasator)
                if check == False:
                    print('Наминало таких купюр нет попробуйте еще')

                file.seek(0,0)
                json.dump(data_incasator,file,indent=4, sort_keys=True)


        return


    outpath = Path.cwd()
    with open(outpath / "users_data", "r") as file_r:
        data = json.load(file_r)
    name = input("Login: ")
    password = input("Password: ")
    usr_type = ''.join([i["type"] for i in data if i['name'] == name])



    user_valid()


start()