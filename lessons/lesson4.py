# инкапсуляция
# открытый  защищенный = _
# скрытый __
class Person:
    def __init__(self, name, old):
        self._name = name
        self.__old = old

    @property
    def get_old(self):
        return self.__old

    @get_old.setter
    def get_old(self, old):
        self.__old = old

    def __str__(self):
        return f"{self._name} {self.__old}"


p = Person('m', 9)
p.get_old = 22


# print(p.get_old)


# p._name = 'бека'
# p._Person__old = 22
# print(p)

# множественное наследование
# MRO-порядок выполнения методов

class A:
    def __init__(self, name):
        self.name = name

    def a(self):
        print('это методот класса А')


# супер класс


class B:
    def __init__(self,age):
        self.age=age
    def a(self):
        print('это методот класса B')


class C(B, A):
    def __init__(self, name,age):
        A.__init__(self,name)
        B.__init__(self,age)


# def a(self):
#     print('это методот класса C')


# дочерний класс

a = C('name',99)
print(a.age,a.name)
a.a()
print(C.mro())






class Checkakk:...

class Savingak:...

class Bankakk(Checkakk, Savingak):...

class Nedvigim:...

class Strahov(Bankakk, Nedvigim):...

class Akcii:...

class Oblegacii:...

class Security(Akcii, Oblegacii):...

class Activi(Bankakk,Security):...

class Procentdohod(Bankakk, Security):...