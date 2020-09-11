# xxx



stringx = 'python ahahaha'

for item in stringx:
  print(item)




stringy = 'python ahahaha'
counter = 1

for item in stringy:
  counter = counter + 1
  print(f'{item} : {counter}')




list1 = ['jen', 'sarah', 'janelle']

for item in list1:
  print(item)




list2 = [1, 2, 3, 4, 5]

for item in list2:
  print(item)



# using range function
for item in range(18):
  print(item)



# with starting number
for item in range(9, 18):
  print(item)



# with interval
for item in range(9, 50, 3):
  print(item)



# sum of items inside an array
prices = [10, 20, 30, 40, 50, 60, 70]
total = 0
for item in prices:
  total = total + item
  print(total)
print(f'final total: {total}')