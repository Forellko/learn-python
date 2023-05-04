students = [{"name": "Vova", "age": "25", "weight": 110},
            {"name": "Gregory", "age": "30", "weight": 70}]


def get_name(student):
    return student["weight"]


print(sorted(students, key=get_name))
