
class Laptop:

    def code(self,ide):
        ide.execute()

class PyCharm:
    def execute(self):
        print('Compiling..')
        print('Executing...')

class VsCode:
    def execute(self):
        print('Spelling Checked')
        print('Compiling..')
        print('Executing...')

ducktype = PyCharm()
duck1 = VsCode()

lap1 = Laptop()
lap1.code(ducktype)
print()

lap1.code(duck1)
