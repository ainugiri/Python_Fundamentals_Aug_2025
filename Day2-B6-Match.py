# how to create a function

#  def keyword function_name (input parameters):
#      function body

def mysum(a,b): # function definition
    return (a-1) + (b-1)    # function body   

# to call the function function_name(input parameters)

val = mysum(10,20)  # function call
print(val)  # This will print 28, as it subtracts 1 from eachcls

# -b + (b^2 - 4ac)^(1/2)) / 2a
def quadratic1(a, b, c):
    result = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    return result
def quadratic2(a, b, c):
    result = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return result

# x^2 -3x + 2 = 0
# a = 1, b = -3, c = 2

x1 = quadratic1(1, -3, 2)  # This will calculate the first root
x2 = quadratic2(1, -3, 2)  # This will calculate the second root
print(f'The roots of the equation are: {x1} and {x2}')

# 1 - Purchase
# 2 - Service
# 3 - Support

userinput = int(input('Enter your choice (1-3): '))
if userinput == 1:
    print('You selected Purchase')  
elif userinput == 2:
    print('You selected Service')
elif userinput == 3:
    print('You selected Support')   
else:
    print('Invalid choice, please select 1, 2, or 3')

inp = input('Enter a value iPhone, OnePlus, Google, HP: ')
print(type(inp))  # This will print <class 'str'> indicating that inp is a string
match inp:
    case 'iPhone' | 'OnePlus' | 'Google' | 'Sony':
        print('You selected mobile device')
    case 'HP' | 'Dell' | 'Lenovo':
        print('You selected Laptop')
    case _:
        print('Invalid choice, please select 1, 2, or 3')


