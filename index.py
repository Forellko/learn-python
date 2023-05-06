class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house


student = Student('Vladimir', 'Taganrog')

print(student.name)
