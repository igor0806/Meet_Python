# 6. Написати скрипт, який об'єднає три словника в самий перший. Оновлюється тільки перший словник. Дані можна

dict_1 = {'car': 'Vw', 'model': 'Touareg'}
dict_2 = {'notebook': 'Mac', 'type': 'Pro'}
dict_3 = {5: 20, 10: 50}
dict_1.update(dict_2)
dict_1.update(dict_3)
print(dict_1)