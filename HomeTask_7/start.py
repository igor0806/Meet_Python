import csv
import json



def start():

    def user_valid():
        try_false = 3
        while try_false != 0:
            user_name = input('Введите имя: ')
            password = input('Введите пароль: ')
            with open('users.data.csv', mode='r', encoding='utf-8') as users_data:
                read_users_data = csv.reader(users_data, delimiter=',')
                all_users = [i for i in read_users_data]
                if [user_name, password] in all_users:
                    return menu(user_name)
                else:
                    try_false -= 1
            print(f'Неправильный пароль или имя!Осталось{try_false} попыток!')

        print(exit_bank())

    def menu(user_name):
        count_false = 3
        while count_false != 0:
            print('Введите действие:\n'
                '1 - Просмотреть баланс\n'
                '2 -  Пополнить баланс\n'
                '3- Снятие средств\n'
                '4 - Выход')
            number_operation = int(input('Введите номер операции: '))
            if 0 <= number_operation <= 4:
                if number_operation == 1:
                    print(balance(user_name))
                elif number_operation == 2:
                    print(money_add(user_name))
                elif number_operation == 3:
                    print(money_give(user_name))
                elif number_operation == 4:
                    print(exit_bank())
                    break
            else:
                count_false -= 1
                print(f'Попробуйте еще{count_false}попыток осталось')

        exit_bank()

    def balance(user_name):
        with open(f'{user_name}_balance.data.csv', mode='r', encoding='utf-8') as users_data:
            read_users_data = csv.DictReader(users_data, delimiter=',')
            for line in read_users_data:
                return int(line['Balance'])

    def money_give(user_name):
        start_balance = balance(user_name)
        money_give = int(input('Введите сумму для снятия: '))
        if money_give <= start_balance:
            new_balance = start_balance - money_give
            with open(f'{user_name}_balance.data.csv', mode='w', encoding='utf-8') as write_balance:
                write = csv.writer(write_balance, delimiter=',')
                write.writerow(['Balance'])
                write.writerow([new_balance])
            result = new_balance

            json_file = {'Operation': 'Withraw', 'Status': 'Succes'}
            new_balance = json.dumps(json_file)
            new_balance = json.loads(str(new_balance))
            with open(f'{user_name}_transactions.data.json', mode='a', encoding='utf-8') as transaction:
                json.dump(new_balance, transaction)

        else:
            return 'Недостаточно денег на вашем счету,введите другую сумму'

        return f'Операция успешна!{result}'

    def money_add(user_name):
        start_balance = balance(user_name)
        amount = int(input('Введите сколько хотите внести: '))
        if amount > 0:
            new_balance = start_balance + amount
            with open(f'{user_name}_balance.data.csv', mode='w', encoding='utf-8') as write_balance:
                write = csv.writer(write_balance, delimiter=',')
                write.writerow(['Balance'])
                write.writerow([new_balance])
            result = new_balance

            json_file = {'Operation': 'Withraw', 'Status': 'Succes'}
            new_balance = json.dumps(json_file)
            new_balance = json.loads(str(new_balance))
            with open(f'{user_name}_transactions.data.json', mode='a', encoding='utf-8') as transaction:
                json.dump(new_balance, transaction)
        else:
            return 'Неверная операция!'

        return f'Операция успешна. На счету{result}!'

    def exit_bank():
        return 'До скорой встречи'

    print('WELCOME')
    user_valid()

start()

