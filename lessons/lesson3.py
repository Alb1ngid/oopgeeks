# инкапсуляция
# открытый защищенный скрытый

class Bank:
    def __init__(self, name, money, key):
        self.name = name
        self._money = money
        self.__key = key

    def get_key(self):
        print(self.__key)

    def set_key(self, password):
        self.__key = password

    def __str__(self):
        return f"name is {self.name}\n" \
               f"{self._money} "

    def password(self):
        self.__a()

    def __a(self):
        print(self.__key)


user1 = Bank('beka', 200_000, 'qwerty')
user1.set_key('000000000')
# user1.get_key()

# user1._money = 10000000000
user1._Bank__key = '12345321'
# print(user1)

# user1.password()
user1._Bank__a()
print(dir(user1))
