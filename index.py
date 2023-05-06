def get_student():
    name = input('name: ')
    house = input('house: ')
    return name, house


name, house = get_student()

print(name, house)
