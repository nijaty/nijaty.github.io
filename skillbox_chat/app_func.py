class User:
    login: str
    age: int
    password: str

    def __init__(self, log, pswd):
        self.login = log
        self.password = pswd


user1 = User("nicat", "")
print(user1.login)
# user1 = User()
# user1.age = 50
#
# user2 = User()
# user2.login = "nicat"
#
#
# print(user1.age)
#
# print(user1.login, user1.password)
# print(user2.login, user2.password)
