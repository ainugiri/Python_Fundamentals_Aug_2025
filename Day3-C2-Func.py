# block of code,
# code reusability
def display():
    print('Hi Hello')
    
display()
display()
display()
display()
display()
display()
display()
display()
display()
display()

def greet(name):
    print(f'Hi {name}!, Welcome to Python')

greet('Giri')
greet('Mohammed')
greet('Jack')

def childDetails(*kids):
    x = len(kids)
    print(f'The number of kids {x}')
    for kid in kids:
        if kid == 'Giri':
            continue
        print(kid)

childDetails('Sam','Yuksha','Yusuf','Giri','Rose','Steve')
childDetails('Gurus')


def printProgram(pname, noofday = 3):
    print(f'{pname} is scheduled for {noofday} days')

printProgram('Python', 3)
printProgram('AWS DevOps', 4)
printProgram('Azure AI Fundamentals', 5)
printProgram('Generative AI')

def ven_dis(vend):
    print("Vendor Information")
    for vendors in vend:
        print(vendors)


vendor_list1 = ['Apple','Dell','HP']
ven_dis(vendor_list1)


def retVal():
    return 19

x = retVal()
print(x)



def areaCircle(rad):
    return 22*rad*rad/7

userInput = float(input("Enter the radius of the circle"))
print(f'The area of circle with radius {userInput} in cm is {areaCircle(userInput)}')
area = areaCircle(21)
print(area)

def withBlock():
    pass