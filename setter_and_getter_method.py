class Customer:
    def __init__(self, cust_id, cust_name, age, wallet_balance):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.age = age
        self.__wallet_balance = wallet_balance

    def set_wallet_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance = amount

    def get_wallet_balance(self):
        return self.__wallet_balance

c1 = Customer(100, 'Gopal', 23, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())