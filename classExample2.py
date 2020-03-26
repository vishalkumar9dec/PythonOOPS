class car:

    wheel = 4

    def __init__(self):
        self.mil = 30
        self.comp = 'BMW'


c1 = car()
c2 = car()

c2.mil = 20

print(c1.mil, c2.comp, c1.wheel)
print(c2.mil, c2.comp, c2.wheel)

car.wheel = 8  #we have updated the class variable

print(c1.mil, c2.comp, c1.wheel)
print(c2.mil, c2.comp, c2.wheel)