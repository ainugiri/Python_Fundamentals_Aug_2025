# Operators
# Arithmetic Operators 
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Modulus %
# Exponentiation **
# Floor Division //

a  =  100
b = 33

print('Addition:', a + b)
print('Subtraction:', a - b)
c = a * b
print('Multiplication:', c) 
print('Division:', a / b)
print('Modulus:', a % b) # remainder of division
print('Exponentiation:', b ** 3) # a raised to the power of b
print('Floor Division:', a // b) # division without remainder

# Assignment Operators
c = 10
print(c)
# c = c + 10
# print(c)  # This will print 20
c += 10
print(c)  # This will print 20
# c = c - 5
c -= 5
print(c)  # This will print 15
# c = c * 2
c *= 2  
print(c)  # This will print 30
# c = c / 3
c /= 3
print(c)  # This will print 10.0

# c = c ** 3 # 1000
c **= 3  # 1000.0
print(c)  # This will print 1000.0


ip1 = int(input('Enter first number: '))     # always consider as string value
# print(type(ip1))  # This will print <class 'str'> indicating that ip
ip2 = int(input('Enter second number: '))
op = ip1 + ip2
print(op) 
#  # Comparison Operators
#  equal to ==
#  not equal to !=
#  greater than >
#  less than <
#  greater than or equal to >=
#  less than or equal to <=
if ip1 == ip2:
    print('Both numbers are equal')
elif ip1 > ip2:
    print('First number is greater than second number')
elif ip1 < ip2:
    print('First number is less than second number')
else: 
    print('Invalid input')


# Logical Operators
# and
# or
# not

#  more than one condition, we can use logical operators
#        cond1   cond2   result
# And    True    True    True
# AND    True    False   False
# AND    False   True    False
# AND    False   False   False

# Or     True    True    True
# Or     True    False   True
# Or     False   True    True
# Or     False   False   False

# NOT   True    False
# NOT   False   True


x = 10
y = 20

if x > 5 and y < 30:
    print('stmt1')
    print('stmt1')
    print('stmt1')
    print('stmt1')
    print('stmt1')
    print('Both conditions are true')
if x > 12 and y < 30: # x is not greater than 12 false and true  -> false -> will not execute
    print('stmt2')
    print('stmt2')
    print('stmt2')
    print('stmt2')
    print('At least one condition is true')

if x > 5 and y < 15: # y is not less than 15 true and false -> false -> will not execute
    print('stmt3')
    print('stmt3')
    print('stmt3')
    print('stmt3')
    print('At least one condition is true')


list1 = ['iPhone', 'OnePlus', 'Google', 'Sony']

x = input('Enter a value to check if it is in list1: ')
if x not in list1:  # Check if x is in list1
    print(f'{x} is NOT in list1')
else:
    print(f'{x} is in list1')

# membership operators
# in
# not in