class Student:
    def __init__(self, name, house, ) -> None:
        self.name = name
        self.house = house

    @property
    def name(self):
        print(1)
        return self._name

    @name.setter
    def name(self, name):
        print(2)
        self._name = name

    @classmethod
    def get(cls):
        return cls()


student = Student('Vladimir', 'Taganrog')

student.name = 'Sasha'

print(student.name)
