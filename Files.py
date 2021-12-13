import csv

with open('admin.data.csv', mode='w', encoding='utf-8') as file:
    file = csv.reader(file, delimiter=',')
    all_users = [i for i in read_users_data]
