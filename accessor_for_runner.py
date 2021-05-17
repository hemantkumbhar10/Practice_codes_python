class Athelete:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def running(self):
        if (self.__gender == 'girl'):
            print('150 m running')
        else:
            print('200 m running')
c1 = Athelete('Maria', 'girl')
print(c1.running())
