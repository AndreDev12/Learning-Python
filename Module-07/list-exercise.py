planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)

number_of_planets = len(planets)
print('There are', number_of_planets, 'planets')

planets.append('Pluto')
print('Actually, there are', len(planets), 'planets')
print(planets[-1], 'is the last planet')