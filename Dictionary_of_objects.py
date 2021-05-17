class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1 = Mobile('apple', 2000)
mob2 = Mobile('samsung', 3400)
mob3 = Mobile('nokia', 5000)
mob4 = Mobile('mi', 4522)

mob_dict = {'m1' : mob1,
            'm2' : mob2,
            'm3' : mob3,
            'm4' : mob4}

for key,value in mob_dict.items():
    if value.price < 3000:
        print(value.brand, value.price)