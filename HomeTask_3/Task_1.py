# 1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову,
# яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.

number = int(input('введите число: '))
print(', '.join(map(str,(x for x in range(0, number ) if x % 17 == 0))))