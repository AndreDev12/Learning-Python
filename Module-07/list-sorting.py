amalthea_moons = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_moons + galilean_moons
regular_satellite_moons.sort()
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

# Para ordenar una lista en orden inverso, llame a .sort(reverse=True) en la lista
regular_satellite_moons.sort(reverse=True)
print('The regular satellite moons of Jupiter are', regular_satellite_moons)