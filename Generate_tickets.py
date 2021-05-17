class Ticket:
    counter = 00
    destination_cities = ['mumbai', 'pune', 'chennai', 'kolkata']
    def __init__(self,source, destination):
        self.__source = source
        self.__destination = destination

    def validate_source(self):
        return (self.__source.lower() == 'delhi')

    def validate_destination(self):
        if any(self.__destination in city for city in Ticket.destination_cities):
            return True
        else:
            return False

    def validate_source_destination(self):
        return self.validate_source() and self.validate_destination()

    def split_word(self):
        city_ini = self.__destination[0]
        city_initial = city_ini.upper()
        return city_initial


    def generate_ticket(self):
        if self.validate_source_destination():
            print('D'+self.split_word()+str(0)+str(Ticket.counter))
            Ticket.counter += 1

t1 = Ticket('delhi', 'mumbai')
(t1.generate_ticket())
t2 = Ticket('delhi', 'kolkata')
t2.generate_ticket()

t3 = Ticket('delhi', 'pune')
t3.generate_ticket()






