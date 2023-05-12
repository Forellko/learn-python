students = [
    {"name": 'Vladimir', "rate": 5},
    {"name": 'Sasha', "rate": 6},
    {"name": 'Roma', 'rate': 7}
]

ratemt5 = filter(lambda student: student["rate"] > 5, students)
ratemt5 = sorted(ratemt5, key=lambda student: student["name"])

print(*ratemt5)