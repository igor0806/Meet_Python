import csv
import json
from time import sleep


def start():
    def valid_login_pass():
        try_false = 3
        while try_false != 0:
            user_name = input("Введите имя пользователя:\n")
            pin = input("Введите пин-код:\n")
            with open("users.data.csv", mode="r", encoding="utf-8") as users_data:
                read_users_data = csv.reader(users_data, delimiter=",")
                all_users_list = [row for row in read_users_data]
                if [user_name, pin] in all_users_list:
                    sleep(0.5)
                    return choosing_operation(user_name)
                else:
                    try_false -= 1
            print("Не правильные имя пяльзователя или пароль!\n"
                          ""
                          f"Осталось {try_false} попыток\n")
                    sleep(0.5)
        sleep(0.3)
        print(exit_bank())

    def choosing_operation(user_name):
        count_false = 5
        while count_false != 0:
            print("Выберете оперецию:\n"
                  "Для просмотра баланса, нажмите - 1\n"
                  "Для снятия денег, нажмите - 2\n"
                  "Для пополнение счета, нажмите - 3\n"
                  "Для выхода, нажмите - 0\n")
            operation_num = int(input("Введите номер операции:\n"))
            if 0 <= operation_num <= 3:
                if operation_num == 1:
                    sleep(0.3)
                    print(f"У Вас на счету {balance_view(user_name)}USD!\n")
                elif operation_num == 2:
                    sleep(0.3)
                    print(take_cash(user_name))
                elif operation_num == 3:
                    sleep(0.3)
                    print(deposite(user_name))
                elif operation_num == 0:
                    sleep(0.3)
                    print(exit_bank())
                    break
            else:
                count_false -= 1
                sleep(0.3)
                print("Не верная операция!\n"
                      ""
                      f"Осталось {count_false} попыток\n")
        sleep(0.3)
        exit_bank()

    def balance_view(user_name):
        with open(f"{user_name}_balance.data.csv", mode="r",
                  encoding="utf-8") as users_data:
            read_users_data = csv.DictReader(users_data, delimiter=",")
            for line in read_users_data:
                sleep(0.3)
                return int(line['BalanceUSD'])

    def take_cash(user_name):
            current_balance = balance_view(user_name)
            take_cash = int(input("Введите сумму для снятия:\n"))
            if take_cash <= current_balance:
                new_balance = current_balance - take_cash
                with open(f"{user_name}_balance.data.csv", "w",
                          encoding="utf-8") as write_balance:
                    writer = csv.writer(write_balance, delimiter=",")
                    writer.writerow(['BalanceUSD'])
                    writer.writerow([new_balance])
                result = new_balance
                j_result = {"Operation": "Withraw", "Status": "Succese", "Current Balance": result}
                new_balance = json.dumps(j_result)
                new_balance = json.loads(str(new_balance))
                with open(f"{user_name}_transactions.data.json", mode="a", encoding="utf-8") as transaction:
                    json.dump(new_balance, transaction)

            else:
                sleep(0.3)
                return f"Недостаточно денег на счету!.\n" \
                       f"Введите другую сумму! На счету {current_balance}\n"
            sleep(0.3)
            return f"Операция успешна!\n" \
                   f"На Вашем счету {result}USD!\n"

    def deposite(user_name):
        current_balance = balance_view(user_name)
        amount = int(input("Enter deposite amount:\n"))
        if amount > 0:
            new_balance = current_balance + amount
            with open(f"{user_name}_balance.data.csv", "w",
                      encoding="utf-8") as write_balance:

                writer = csv.writer(write_balance, delimiter=",")
                writer.writerow(['BalanceUSD'])
                writer.writerow([new_balance])
            result = new_balance
            j_result = {"Operation":"Deposite", "Status":"Succese", "Current Balance":result}
            new_balance = json.dumps(j_result)
            new_balance = json.loads(str(new_balance))
            with open(f"{user_name}_transactions.data.json", mode="a", encoding="utf-8") as transaction:
                json.dump(new_balance, transaction)
        else:
            sleep(0.3)
            return "Неверная Операция"
        sleep(0.3)
        return f"Операция успешна!\n" \
               f"На Вашем счету {result}USD!\n"

    def exit_bank():
        return f"*** Спасибо за использование GeegHub-Bank ***\n"\
               "*** Хорошего дня и не забывайте улыбаться! ***"

    print("*** Добро пожаловать в GeekHub-Bank ***")
    sleep(0.5)
    valid_login_pass()

start()