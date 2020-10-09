for y in range(1,10):
    str_x = ''
    for x in range(y,10*y,y):
        if x < 10:
            str_x += str(x) + '  '
        else:
            str_x += str(x) + ' '
    print(str_x)