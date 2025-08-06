str1 = 'Python is a prog'
# 0 - p
# 1 - y
# 2 - t
# 3 - h
# 4 - o
# 5 - n
# 6 - ' '
# 7 - i
# 8 - s
# 9 - ' '
# 10 - a
# 11 - ' '
# 12 - p
# 13 - r
# 14 - o
# 15 - g

str2 = str1[12:16]  # Extracting 'prog' from str1
print(str2)  # This will print 'prog'


str3 = str1[:6] # Extracting 'Python' from str1
print(str3)  # This will print 'Python'

str4 = str1[7:]  # Extracting 'is a prog' from str1
print(str4)  # This will print 'is a prog'

str5 = str1[10]  # Extracting 'a' from str1
print(str5)  # This will print 'a'

print(str1.upper())  # This will print 'PYTHON IS A PROG'
print(str1.lower())  # This will print 'python is a prog'


# def chatbot():
#     print('Hello, how can I help you?')
#     userInput = input('User:')
#     if(userInput.lower() == 'hi' || userInput.lower() == 'hello'):
#         print('Chatbot: Hello! How can I assist you today?')
#     else : 
#         print('Chatbot: I am not sure how to respond to that. Can you please rephrase?')
# chatbot()

str6 = '             Giri Prasad P               '
print(str6)
print(str6.strip())  # This will print 'Giri Prasad P' without leading and trailing spaces

str7 = str6.replace('i','u')
print(str7)  # This will print 'Guru Prasad P' with 'i' replaced by 'u'
str7 = str7.strip()  
print(str7)  # This will print 'Guru Prasad P' with 'i' replaced by 'u'

str8 = 'Python, C++, Java, JavaScript'
print(str8)  # This will print 'Python, C++, Java, JavaScript'
print(type(str8))  # This will print <class 'str'> indicating that str8 is a string
str9 = str8.split(', ')  # This will split the string into a list of languages
print(str9)  # This will print ['Python', 'C++', 'Java', 'JavaScript']
print(type(str9))  # This will print <class 'list'> indicating that str9 is a list  

fname = 'Giri'
lname = 'Prasad'
# # fullname = fname + lname  # Concatenating first name and last name
# fullname = fname + " " + lname  # Concatenating first name and last name
fullname = fname + ' ' + lname  # Concatenating first name and last name
print(fullname)  # This will print 'Giri Prasad'

str10 = "Python's features are great,\n \"1. Simple\" and \n \"2. Powerful\""

print(str10)  # This will print Python's features are great, "1. Simple" and "2. Powerful"

print('DAS ID \t\t Name \t Mobile \t City')
print('A825662 \t Giri \t 9876543210 \t Bangalore')
print('A825662 \t Giri \t 9876543210 \t Bangalore')
print('A825662 \t Giri \t 9876543210 \t Bangalore')
print('A825662 \t Giri \t 9876543210 \t Bangalore')
print('A825662 \t Giri \t 9876543210 \t Bangalore')


name = input("Enter your name:")
print(name)
print(name.find('r'))
print(name.swapcase())