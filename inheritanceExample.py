class A:

    def __init__(self):
        print('A init')

    def feature1(self):
        print('Feature 1')

    def feature2(self):
        print('feature2')

class B():

    def __init__(self):
        print('B init')

    def feature3(self):
        print('Feature 3')

    def feature4(self):
        print('feature4')

class D :
    def __init__(self):
        print('D init')

    def feature5(self):
        print('Feature 5')

class E(B,D):

    def __init__(self):
        super().__init__()
        print('E init')

    def feature6(self):
        print('Feature 6')




e1 = E()



