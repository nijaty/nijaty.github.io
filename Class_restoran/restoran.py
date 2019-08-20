class Restoran:
    
    

    def __init__(restoran, name):
        restoran.name = name
        restoran.isci_sayi = 0

class Isciler(Restoran):

    def __init__(isci, name, salary, surname, id, restoran):
        isci.name = name
        isci.salary = salary
        isci.surname = surname
        isci.id = id
        isci.restoran = restoran
        restoran.isci_sayi += 1
        

neon = Restoran("Neon")
aydin_2056 = Isciler("Aydin", "200", "Semedzade", "2056", neon)
aydin_2057 = Isciler("Aydin", "200", "Semedzade", "2057", neon)
ay_isigi = Restoran("Ay isigi")

print("Iscinin adi: " + aydin_2056.name)
print("Restoranin adi: " + ay_isigi.name)
print("Restoranin adi: " + neon.name)
print(aydin_2056.name + "in maashi:  " + aydin_2056.salary + " AZN")
print(aydin_2056.name + "in islediyi restoranin adi: " + aydin_2056.restoran.name)
print(aydin_2056.name + "in"+  " ID-si: " + aydin_2056.id)
print(aydin_2057.name + "in"+  " ID-si: " + aydin_2057.id)


