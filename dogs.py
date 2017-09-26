dogs = ['Scruffy', 'Fido', 'Rover', 'Pete']

def print_dogs_in_tow(dogs_list):
    dogs_to_print = 'Dogs in tow: '

    for dog in dogs_list:
        dogs_to_print += dog + ', '

    dogs_to_print = dogs_to_print[0:-2] + '\n'
    print(dogs_to_print)


print_dogs_in_tow(dogs)

print("I'm'a go pick up some dogg")
dogs.append('Beatrix')
print_dogs_in_tow(dogs)

print("I'm'a go drop off my first dogg %s." % dogs[0])
dogs.pop(0)
print_dogs_in_tow(dogs)

print("I'm'a go drop off my last dogg %s." % dogs[-1])
dogs.pop(-1)
print_dogs_in_tow(dogs)