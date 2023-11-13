# Crear una lista
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)

# Acceso a elementos de lista por índice
print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])

# Modificar valor de la lista
planets[3] = 'red planet'
print('Mars is also known as', planets[3])

# Determinación de la longitud de una lista
number_of_planets = len(planets)
print('The are', number_of_planets, "planets in the solar system.")

# Incorporación de valores a listas
planets.append('Pluto')
number_of_planets = len(planets)
print('There are actually', number_of_planets, 'planets in the solar system.')

# Eliminación del último elemento de una lista
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets.pop()
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')

# Uso de índices negativos
print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])

# Búsqueda de un valor en una lista
jupiter_index = planets.index('Jupiter')
print('Jupiter is the', jupiter_index + 1, 'planet from the sun')

mercury_index = planets.index('Mercury')
print('Mercury is the', mercury_index + 1, 'planet from the sun')