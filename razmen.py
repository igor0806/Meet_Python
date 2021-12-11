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