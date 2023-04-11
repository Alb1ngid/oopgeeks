# Парадигмы ооп
# наследование-полиморфизм

class Human:  # супер класс
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} runs')


class Student(Human):  # дочерний класс
    def run(self):
        print(f'{self.name} fly')

    def fale(self):
        print('fale')


class Batrak(Student):
    def __init__(self, name, age, last):
        # Human.__init__(self,name,age)
        super().__init__(name, age)
        self.last = last

    def new(self):
        Human.run(self)
        super().run()


c = Batrak('адахан', 18, 'last')
c.new()

human = Human('beka', 19)
student = Student('станислав', 11)
student.run()
human.run()

print(Batrak.mro())

print(object)


