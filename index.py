students = [
    {"name": 'Vladimir', "rate": 5},
    {"name": 'Sasha', "rate": 6},
    {"name": 'Roma', 'rate': 7}
]

ratemt5 = filter(lambda student: student["rate"] > 5, students)

print(*ratemt5)