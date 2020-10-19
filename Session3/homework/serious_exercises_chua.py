sheeps = [5,10,40,50]

max_number = sheeps[0]

for sheep in sheeps:
    if max_number < sheep:
        max_number = sheep

print(max_number)