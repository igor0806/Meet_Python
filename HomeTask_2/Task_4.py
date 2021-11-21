# 4.Write a script to concatenate following dictionaries to create a new one

dict_1 = {'car': 'Vw', 'model': 'Touareg'}
dict_2 = {'notebook': 'Mac', 'type': 'Pro'}
dict_3 = {5: 20, 10: 50}
dict_4 = {}
for n in (dict_1, dict_2, dict_3): dict_4.update(n)
print(dict_4)
