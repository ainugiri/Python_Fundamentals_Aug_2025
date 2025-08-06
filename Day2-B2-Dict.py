# key - value pairs

A825662 = dict()
A825662 = {
    'name':'Giri',
    'age': 30,
    'role': 'Developer',
    'city': 'Bangalore'
}
print(A825662)
print(A825662['name'])
print(A825662.get('city'))

print(A825662.get('mobile','Not Found'))
# print(A825662['mobile'])  # This will raise an error if 'mobile' key does not exist

A825662['age'] = 40
A825662['mobile'] = '9876543210'
A825662['Country'] = 'India'
A825662['skills'] = ['Python', 'Java', 'C++']
print(A825662)

print(A825662.get('skills'))

# to print all keys
print(A825662.keys())

# to print all values
print(A825662.values())

print(A825662.items()) # print all key-value pairs

A825662.update({'Country': 'USA'})  # Update the value of 'Country'
print(A825662)
A825662.update({'Country': 'India', 'exp': 5 })  # Update the value of 'Country'
print(A825662)

A825662.pop('exp')  # Remove the key 'exp'
print(A825662)

A825662.popitem()  # Remove the last inserted key-value pair
print(A825662)

del A825662['mobile']

print(A825662)

A825663 = A825662.copy()
print(A825663)
A825663['name'] = 'Ravi'
print(A825663)

print(len(A825662))  # Length of the dictionary

A825662.clear()  # Clear all items in the dictionary
print(A825662)  # This will print an empty dictionary

# del A825662  # Delete the dictionary completely
# print(A825662) # This will raise an error because A825662 is deleted

A825662.clear()
print(A825662)  # This will print an empty dictionary
del A825662
# This will raise an error because A825662 is deleted
# print(A825662)  # Uncommenting this line will raise an error because A825662 is   
# deleted
print(A825662)
