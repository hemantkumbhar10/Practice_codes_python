class Shoe:
    def __init__(self, price, material):
        self.price = price
        self.material = material

    def __str__(self):
        return 'The price of shoe is' + ' ' + str(self.price) +  ' ' + 'and material is ' + self.material

s1 = Shoe(3000+20, ' leather')
print(s1)