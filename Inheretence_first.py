class Phone:
    def __init__(self, brand, price, camera):
        self.brand = brand
        self.price = price
        self.camera = camera

    def buy(self):
        print('Buying the phone')
    def return_phone():
        print('Returning the phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print("Inside the Smartphone Constructor")

    def buy(self):
        print('Buying the Smartphone')

s = Phone('Android', 2000, '13px')
S = SmartPhone('linux', 4)
print(s.brand)
