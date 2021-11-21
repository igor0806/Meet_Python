# 2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення

input_list = input("Type value: ")
List_of_tuples = [(10, 20, 40, 'car'), (40, 50, 'green', 60), (70, 80, 90, 'cool')]

list_number = []

for i in List_of_tuples:
    new_val = list(i)
    new_val[-1] = input_list
    changeList = tuple(new_val)
    list_number.append(changeList)
print(list_number)

