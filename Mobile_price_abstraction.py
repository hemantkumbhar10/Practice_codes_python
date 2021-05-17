class Mobile:
    def __init__(self,price, brand):
        print('Inside the constructor')
        self.price = price
        self.brand = brand

    def purchase(self):
        print('Inside the purchase')
        print('The mobile brand is', self.brand, 'and the price is ', self.price)

m1 = Mobile(10000, 'Xiaomi')
m1.purchase()