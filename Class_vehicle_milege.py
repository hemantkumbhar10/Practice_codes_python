class Vehicle:
    def __init__(self):
        print('Inside Constructor')

    def identify_distance_that_can_be_travelled(self, fuel_left, mileage):
        self.fuel_left = fuel_left
        self.mileage = mileage
        if self.fuel_left > self.reserve_fuel:
            fuel = self.fuel_left - self.reserve_fuel
            

