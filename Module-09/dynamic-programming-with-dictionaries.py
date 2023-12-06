# Recuperación de todas las claves y valores
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for month in rainfall.keys():
    print(f'{month}: {rainfall[month]}cm')

# Determinación de la existencia de una clave en un diccionario
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
print(rainfall) # {'october': 3.5, 'november': 4.2, 'december': 3.1}

# Recuperación de todos los valores
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value
print(f'There was {total_rainfall}cm in the last quarter.')