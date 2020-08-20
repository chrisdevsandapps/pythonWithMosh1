

course = 'Python for Beginners'

# printing length:
print(len(course))

# convert to upper case
x1 = course.upper()
print(x1)

# convert to lowercase
x2 = course.lower()
print(x2)


# find a certain string
x3 = course.find('P')
print(x3)
x4 = course.find('i')
print(x4)
x5 = course.find('for')
print(x5)


# replace
x6 = course.replace('P', 'J')
print(x6)
x7 = course.replace('for', 'hehehe')
print(x7)


# para makita kung nandun ba yung string na yun sa isang variable
print('Python' in course)

print('Jython' in course)