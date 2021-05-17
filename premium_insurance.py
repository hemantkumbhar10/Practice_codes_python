class Premium:
    def __init__(self, vech_type, price):
        self.vech_type = vech_type
        self.price = price

    def pricce(self):
        if self.vech_type == 'two wheeler':
            p = (self.price/100)*0.2
        else:
            p = (self.price/100)*0.6
        return p

pr = Premium('two wheeler', 20000)
print(pr.pricce())

