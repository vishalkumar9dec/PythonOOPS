class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.model = "HP"
            self.ram = '8GB'
        def show(self):
            print(self.model, self.ram)



s1 = Student('Vishal', 7)
s1.show()