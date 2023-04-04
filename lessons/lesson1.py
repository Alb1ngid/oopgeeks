# ООП - обьектно ориентированное программирование


def a(arg):
    print(arg)


# a('hello')

s = 1


class Human:
    brain = True  # свойства класса

    def __init__(self, name, age, hobby):
        self.named = name
        self.age = age
        self.hobby = hobby

    def __str__(self):
        return f'name is {self.named}\n' \
               f'age is {self.age} \n' \
               f'hobby-{self.hobby}'

    def __len__(self):
        return len(self.named)




    def name(self):  # метод
        print(self.named)


human = Human('Радмир',18,True)
human1 = Human('аделина',16,True)
human2 = Human('Дарига',15,True)
human3 = Human('Эрмек',22,True)
human4 = Human('Арслан',15,True)
human5 = Human('Сергей',44,True)

# human4.name()

print(human1)

print(len(human5))
