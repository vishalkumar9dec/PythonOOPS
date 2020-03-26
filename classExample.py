class configuration:

    def __init__(self,ram,cpu):
        #this method is called automatically.
        #print('in the init method')
        self.ram = ram
        self.cpu = cpu

    def config(self):
        print("RAM : ", self.ram, "GB, CPU : ",self.cpu)



obj1 = configuration(16,'i5')

obj1.config()
