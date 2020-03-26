class Student:
    school = "KV ONGC"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1+self.m3+self.m2)/3

    @classmethod
    def get_school(cls):
        print(cls.school)

    @staticmethod
    def info():
        return "This is just an information method"


s1 = Student(34,56,43)
s2 = Student(56,42,13)

print(s1.average())
print(s2.average())

Student.get_school()
print(Student.info())