'''The below example is for method overloading
if we uncomment the code it will work fine'''
# class summation:
#
#     def add(self,a=None,b=None,c=None):
#         s=0
#         if a!=None and b!=None and c!=None:
#             s = a + b + c
#             return s
#         elif a!=None and b!=None:
#             s=a+b
#             return s
#         else:
#             s=a
#             return s
#
# a = summation()
#
# print(a.add(3))

'''Method Overriding'''

class A:
    def show(self):
        print('in A show')


class B(A):
    #pass
     def show(self):
         print('in B show')

b = B()
b.show()