mon_an1 = 'phở'
mon_an2 = 'cơm'
mon_an3 = 'bún'
mon_an4 = 'thịt chó'


#list

foods = ['phở','cơm','bún','thịt chó',1, True, []]
print(foods[1])

print('1. _____________________')
for i in range(6):
    print(foods[i])
print(foods)
print('1. _____________________')

print('2. _____________________')
for food in foods:
    print(food)
print(foods)
print('2. _____________________')

print('3. _____________________')
for i in range(len(foods)):
    print(i, foods[i])
print('3. _____________________')

print('4. _____________________')
a = foods + ['cơm rang']
print(a)
print('4. _____________________')

#CREATE
print('5. _____________________')
foods.append('bánh bao')
for i in range(len(foods)):
    print(i, foods[i])
print('5. _____________________')

print('6. _____________________')
# a = input('Enter new item')
# foods.append(a)
# for i in range(len(foods)):
#     print(i, foods[i])
print('6. _____________________')
#CREATE

#UPDATE
print('7. _____________________')
foods[4] = 'thịt bò'
for i in range(len(foods)):
    print(i, foods[i])
print('7. _____________________')

#DELETE
foods.remove('phở')  #DELETE by value
foods.pop(0) #DELETE by index
removed_item = foods.pop(0) #DELETE by index and save to variable
print('removed item', removed_item)
print('index',foods.index('thịt bò'))
for i in range(len(foods)):
    print(i, foods[i])
#DELETE


print('bún đậu' in foods)