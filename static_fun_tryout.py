a = input('enter city name :')
destination_cities = ['mumbai', 'pune', 'chennai', 'kolkata']

if any(a in i for i in destination_cities):
    print(a, 'is valid')
else:
    print(a, 'is not valid')

