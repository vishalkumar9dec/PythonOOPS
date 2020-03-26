class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        mk1 = self.m1 + other.m1
        mk2 = self.m2 + other.m2
        s3 = Student(mk1,mk2)
        return '{} {}' .format(mk1,mk2)

    def __gt__(self, other):
        mk1 = self.m1 + self.m2
        mk2 = other.m1 + other.m2

        if mk1 > mk2:
            return True
        else:
            return False

s1 = Student(10,20)
s2 = Student(30,40)

s3 = s1 + s2
print(s3)

if s1 > s2:
    print ('S1 is better')
else:
    print('S2 is better')