import csv

with open('HomeTask_7/Igor_balance.data.csv', mode='w', encoding='utf-8') as file:
    file = csv.reader(file, delimiter=',')
    all_users = [i for i in read_users_data]
    # if [user_name, password] in all_users:
    #     return menu(user_name)