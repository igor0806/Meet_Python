def GetMoney(m, nom_list):
            m = int(m)
                if m < 0:
                    print “m - Incorrect value”
                return
                        nom_list = nom_list.sort(reverse=True)
                        res = {}
                    for nom in nom_list:
                        num = m / nom
                        res = num
                        m = m - nom * num
                    if m:
                    print “Can not find solution”
                        return
                return res

from itertools import product
from operator import mul

n = int(input())

f = lambda tpl: sum(map(mul, tpl, (1, 2, 5, 10)))
count = sum(x == n for x in map(f, product(range(n + 1), range(n // 2 + 1), range(n // 5 + 1), range(n // 10 + 1))))
print(count)