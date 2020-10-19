import math
initial = int(input('How many B bacterias are there?: '))
time = int(input('How much time in minutes will we wait?: '))
total = initial*(2 ** math.floor(time/2))
print('After', time, 'minutes, we will have', total, 'bacterias')