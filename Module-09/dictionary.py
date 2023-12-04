planet = {
    'name': 'Earth',
    'moons': 1
}

# Lectura de valores de diccionario
print(planet.get('name'))
print(planet['name'])

# Modificación de valores de diccionario
# planet.update({'name': 'Makemake'})
# planet['name'] = 'Makemake'
# Uso de la actualización
planet.update({'name': 'Jupiter','moons': 79})
# Uso de corchetes
planet['name'] = 'Jupiter'
planet['moons'] = 79
print(planet)

# Adición y eliminación de claves
planet['orbital period'] = 4333
planet.pop('orbital period')
print(planet)

# Tipos de data complejos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')