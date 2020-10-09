n = int(input('Enter a number: '))

for y in range(1,n+1):
    str_x = ''
    for x in range(y,(n+1)*y,y):
        if x < 10:
            str_x += str(x) + '  '
        else:
            str_x += str(x) + ' '
    print(str_x)