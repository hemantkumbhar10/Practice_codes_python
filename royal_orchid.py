class Flower:
    flower_names = {'orchid':15, 'rose':25, 'jasmin':40}
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
        self.__required_quanitiy = None

    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name
    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg
    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available
    def set_required_quantity(self,required_quantity):
        self.__required_quanitiy = required_quantity

    def get_flower_name(self):
        return self.__flower_name
    def get_price_per_kg(self):
        return self.__price_per_kg
    def get_stock_available(self):
        return self.__stock_available
    def get_required_quantity(self):
        return self.__required_quanitiy

    def validate_flower(self):
        return any(self.__flower_name in key for key in Flower.flower_names)

    def validate_stock(self):
        return self.__stock_available >= self.__required_quanitiy

    def sell_flower(self):
        if self.validate_flower() and self.validate_stock():
            self.__stock_available -= self.__required_quanitiy
            return self.__stock_available
        else:
            return 'Invalid data'

    def check_level(self):
        for key,value in Flower.flower_names.items():
            if self.validate_flower():
                if value >= self.sell_flower():
                    return True
                else:
                    return False

f1 = Flower()
f1.set_flower_name('orchid')
f1.set_stock_available(25)
f1.set_required_quantity(50)
print(f1.validate_flower())
print(f1.validate_stock())
print(f1.sell_flower())
print(f1.check_level())





