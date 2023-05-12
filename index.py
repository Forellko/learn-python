students = [
    {"name": 'Vladimir', "rate": 5},
    {"name": 'Sasha', "rate": 6},
    {"name": 'Roma', 'rate': 7}
]

rate6 = [student['name'] for student in students if student['rate'] == 6]

print(rate6)