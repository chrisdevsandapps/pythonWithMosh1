

# String

# using double quote
course1 = "'python's course"
print(course1)

course2 = 'python for "beginners"'
print(course2)


# multi line
multiline = '''
hahaha
this is a multi ine string
'''
print(multiline)


# index in the string
testindex1 = 'python for beginners'
print(testindex1[0])
print(testindex1[1])
print(testindex1[6]) # space
print(testindex1[7]) # f
print(testindex1[-1]) # s
print(testindex1[-2]) # r
print(testindex1[0:3]) # pyt
print(testindex1[12:3]) # bakit walang output ito?
print(testindex1[0:])
print(testindex1[2:])
print(testindex1[:]) # assumes zero 


aaa = 'hahaha hehehe'
eee = aaa[:]
print(aaa)
print(eee)