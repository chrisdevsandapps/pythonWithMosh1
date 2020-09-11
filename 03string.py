

# String

# using double quote
course1 = "'python's course"
print(course1)

course2 = 'python for "beginners"'
print(course2)


# multi line
multiline = '''
hahaha
this is a multi line string
hehehe
'''
print(multiline)


# index in the string
testindex1 = 'python for beginners'
print(testindex1[0]) # p
print(testindex1[1]) # y
print(testindex1[6]) # space
print(testindex1[7]) # f
print(testindex1[-1]) # s
print(testindex1[-2]) # r
print(testindex1[-3]) # e
print(testindex1[0:3]) # pyt
print(testindex1[0:4]) # pyth
print(testindex1[3:13]) # hon for be
print(testindex1[0:]) # python for beginners
print(testindex1[2:]) # thon for beginners
print(testindex1[:]) # assumes zero, therefore: python for beginners


aaa = 'hahaha hehehe'
eee = aaa[:]
print(aaa)
print(eee)