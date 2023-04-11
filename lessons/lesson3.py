# инкапсуляция
# открытый защищенный скрытый
class Bank:
    def __init__(self, name, money, key):
        self.name = name
        self._money = money
        self.__key = key

    def __str__(self):
        return f"name is {self.name}\n" \
               f"{self._money} "

    def password(self):
        self._a()

    def _a(self):
        print(self.__key)


user1 = Bank('beka', 200_000, 'qwerty')
user1._money = 10000000000
# user1.__key = '12345321'
print(user1)

user1.password()
print(dir(user1))
# print(dir(Bank))
