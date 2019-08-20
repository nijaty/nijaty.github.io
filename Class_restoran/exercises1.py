"""
OOP nin Abstraction

# """


# class Base: 
#     def __str__(self):
#         return "Info about object"


# base = Base()

# '__call__'
# '__new__'
# '__init__'

# print(base)


# Abstraction example 


class People:
    def get_full_name(self):
        pass

    def get_info(self):
        pass

class Worker(People):
    def __init__(self, name, surname):
        pass
    
worker = Worker("Nicat", "Yusubov")
print(worker)