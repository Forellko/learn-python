students = [
    {"name": 'Vladimir', "rate": 5},
    {"name": 'Sasha', "rate": 6},
    {"name": 'Roma', 'rate': 7}
]

universum = [{student["name"]: "Universum"} for student in students]

print(universum)