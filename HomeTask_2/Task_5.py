# 5. Write a script to remove duplicates from Dictionary.

car_garage = {'Vw':
                  {'model': ['Touareg'],
                   'color': ['Grey'],
                   'type': ['SUV']},
              'Seat':{
                  'model': ['Alhambra'],
                  'color': ['Blue'],
                  'type': ['Minivan']},

              'Audi':{
                  'model': ['A6'],
                  'color': ['Black'],
                  'type': ['Sedan']},
              'Skoda':{
                  'model': ['Alhambra'],
                  'color': ['Blue'],
                  'type': ['Minivan']},
              }
result = {}

for key, value in car_garage.items():
    if value not in result.values():
        result[key] = value
print(result)

