#  classX - xyz functionalities
#  childClassY of classX ->  xyz functionalities apply

class GP:
    def hello(self):
        print('Hi, Grand Parent Welcomes you to the session')
class P(GP):
    def hi(self):
        print('Hi, Parent Welcomes you to the session')
class C(P):         # C is child of p1,p2
    def hello(self):
        print('Hello, Child')

obj1 = C()
obj1.hello()
obj1.hi()


# type : Single, Multiple, Multilevel, Hybrid

