planet_name = input("Enter a planet name: ").lower()
# my very elegant mother showed us just nine
inner_planets = ['mercury', 'venus', 'earth', 'mars']
jovian_planets = ['saturn', 'uranus', 'jupiter', 'neptune']

if planet_name in inner_planets:
    print("%s is an inner planet" % planet_name)
elif planet_name in jovian_planets:
    print("%s is a jovian planet" % planet_name)
else:
    print("%s is not a planet." % planet_name)

'''
Output: python3 chapter3_1_planet.py

Enter a planet name: abcd
abcd is not a planet.

Enter a planet name: Jupiter
jupiter is a jovian planet

Enter a planet name: Earth
earth is an inner planet
'''
