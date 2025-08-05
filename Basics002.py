x = 1
y = 2
z = 3
print(x,y,z)

a825662, a825663, a825664 = 'Giri', 'Sakthi', 'Steve'
print(a825662, a825663, a825664)


'''
numeric int, float, complex
'''

x = 3 -3j
print(x)
print(type(x))
print(x.real, x.imag)


'''
Sequence types: list, tuple, range
list 
     1. iPhone
     2. Samsung
     3. OnePlus
     4. iPhone
     list - modify, have duplicates, ordered
'''

list1 = ['iPhone', 'Samsung', 'OnePlus', 'iPhone']
        # 0         1          2         3
print(list1)

print(list1[2])     

# modify
list1[1] = 'Oppo'
print(list1)
list1.append('Samsung')
print(list1)

list1.insert(2, 'Moto')
print(list1)

list1[1] = 'Acer'
print(list1)

print("the total elements in the list are: ", len(list1))

list2 = list()
print(type(list2))
print(list2)

list3 = list1.copy()
print(list3)
list4 =list3[2:4]
print(list4)

print(list3[1:4])

print(list3)
list3.remove('iPhone')
# remove the first occurrence of the value
print(list3)
list3.pop()
list3.pop(3)
print(list3)

list3.clear()
print(list3)

print(list1)
print('Hello World')

list1.sort()
print(list1)

list1.reverse()
print(list1)

list3.clear()
print(list3)

del list1[2]
print(list1)

list2 = ['Acer', 'Dell', 'HP']
list1 = ['Lenovo', 'Asus', 'Apple']
list3 = list1 + list2
print(list3)

#  list is mutable, can be modified
#  ordered, allows duplicates
#  access by index, modify, add, remove elements
#  can be nested, can contain different data types