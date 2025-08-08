# while 
# for
# while - condition : then execute block of code; increment or decrement the value which is in condition

print('Welcome')
print('Welcome')
print('Welcome')
print('Welcome')
print('Welcome')
print('Welcome')

i = 0
userInput = int(input('Enter a number (0 -100): '))

while i < 100:
    print(i)
    i += 1
    if(i == userInput):
        print(f"User wants to exit at {userInput} now the i value is {i}")
        break
print('End of while loop')



while True:
    print('Welcome')
    userInput = int(input('Enter the option (1, Sales 2. Product 3. Service): '))
    match userInput:
        case 1:
            print('You selected Sales')
        case 2:
            print('You selected Product')
        case 3:
            print('You selected Service')
        case _:
            print('Invalid choice, please select 1, 2, or 3')
    userInput = input('Do you want to continue? (yes/no): ')
    if userInput.lower() != 'yes':
        print('Exiting the loop')
        break
    else :
        print('Continuing the loop')



#  while must execute once, decide based on condition inside while block, w.r.t. return True or False.

while True:
    userInput = int(input('Enter a number (0 - 100): '))
    if userInput < 10:
        print(userInput)
        continue  # Skip the rest of the loop and start the next iteration
    else:
        break

#  continue, break - 
#  continue - skip current iteration and continue with the next iteration
# break - exit the loop immediately

count = 0
while count < 100:    
    count += 5
    if count == 25:
        break
    print(count)



#  For Loop
#  iterate over a squence 
purchased_Items = ['iPhone', 'Samsung','Moto']
for items in purchased_Items:
    print(items)

for char in 'PYTHON':
    if char == 'O':
        continue
    print(char)

for numbers in range(5,50,3):
    print(numbers)

for x in range(10):
    print(x)
else:
    print('All the range of values are processed')



noofdays = [2,3,4,5]
programs = ['GenAI', 'ML', 'Python']
for days in noofdays:
    for tp in programs:
        print(f'{days} days training on {tp}')

if count > 20:
    # code later
    pass