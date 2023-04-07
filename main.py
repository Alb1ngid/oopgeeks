class A:
    a = 1

    def a1(self):
        print(self.a)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


a = A('name', 11)
print(a)
