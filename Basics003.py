# protect data from being overwritten, 
# collection of items,not modified

list1 = ['iPhone', 'OnePlus', 'Google', 'Sony']
list1[1] = 'Oppo'
print(list1)

#  TUPLE
tuple1 = ('iPhone', 'OnePlus', 'Google', 'Sony')
print(tuple1)
print(tuple1[2])
# tuple1[1] = 'Oppo'  # This will raise an error because tuples are immutable
print(tuple1)



t1 = (1, 2, 3, 4, 5, 1,2,23,3)
print(t1)


t2 = ('Giri')
print(t2)  # This will print 'Giri' as a string, not a tuple
print(type(t2))

t2 = ('Giri',)
print(t2)  # This will print a tuple with one element
print(type(t2))

t3 = tuple()
t3 = (10,20,30,40,50)
# t3[3] = 100  # This will raise an error because tuples are immutable

for item in t3:
    print(item)


l3 = list(t3)
l3[2] = 100
t3 = tuple(l3)
print(t3)
