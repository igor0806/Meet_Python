# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

def dickt(string):
    n = {}
    for i in string:
        if i in n:
            n[i] += 1
        else:
            n[i]=1
    for i in n:
        print(f"{i} repeats {n.get(i)} times")

yourString = input('Insert  values: ').replace(" ","")
yourList = yourString.split(",")
dickt(yourList)
