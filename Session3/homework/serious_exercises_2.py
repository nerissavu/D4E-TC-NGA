#1
sheeps = '5 7 300 90 24 50 75'

#2.1
list_sheep = sheeps.split(' ')
for i in range(0, len(list_sheep)): 
    list_sheep[i] = int(list_sheep[i]) 
print('Hello, my name is Hiep and these are my chip sizes', list_sheep)

#2.2
print('Now my biggest sheep has size',max(list_sheep),"let's shear it")

#2.3
# list_sheep[list_sheep.index(max(list_sheep))] = 8
# print('After shearing, here is my flock', list_sheep)


#2.4
# for i in range (0, len(list_sheep)):
#     list_sheep[i] += 50
# print('One month has passed, now here are my flock', list_sheep)

#2.5
for i in range(3):
    list_sheep[list_sheep.index(max(list_sheep))] = 8
    print('After shearing, here is my flock', list_sheep)
    print('MONTH',i+1)
    for i in range (0, len(list_sheep)):
        list_sheep[i] += 50
    print('One month has passed, now here are my flock', list_sheep)
  

#2.6
total_size = sum(list_sheep)
print('My flock has size in total:', total_size)
total_money = total_size*2
print('I would get', total_size,'* 2$ =', total_money)