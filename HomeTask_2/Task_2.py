# 2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.

dict_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([n[:-1] + (100,) for n in dict_list])