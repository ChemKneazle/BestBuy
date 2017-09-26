dogs = ['Scruffy', 'Fido', 'Rover', 'Pete']
for dog in dogs:
    print(dog)

print("I'm gonna go pick up some dogs")

dogs.append('Beatrix')
for dog in dogs:
    print(dog)

print("I'm gonna output a range of dogs")

specialdogs = dogs[-1:1]

for dog in specialdogs:
    print(dog)