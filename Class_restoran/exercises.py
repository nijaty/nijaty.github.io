class Home:
    about = "Bu bina yeni tikilidir"
    floor = 4
    evlerin_sayi = 0


    def __init__(self, name, area):
        self.name = name
        self.area = area
        Home.evlerin_sayi +=1


    @classmethod
    def get_class(cls):
        print(cls)
        print("Umumi evlerin sayi", cls.evlerin_sayi)


    def info(self):
        print(f"My {self.name} area is {self.area}")

home = Home("Guneshli", "200")
home2 = Home("Melissa", "100")

print(home.info())
print(Home.get_class())
    