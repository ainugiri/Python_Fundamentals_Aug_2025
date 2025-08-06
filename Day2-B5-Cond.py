#  logical operators
#  and or not
x = int(input('Enter the value for x: '))
y = int(input('Enter the value for y: '))
if x > 5 and y < 30:
    print('stmt1')
    print('stmt1')
    print('stmt1')
    print('stmt1')
    print('stmt1')
    print('BOTH conditions are true')
if x > 12 or y < 30: # x is not greater than 12 false and true  -> true -> will execute
    print('stmt2')
    print('stmt2')
    print('stmt2')
    print('stmt2')
    print('At least one condition is true')

