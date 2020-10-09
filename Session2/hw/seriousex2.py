n = int(input('n: '))

while True:
    m = 1
    for i in range(1, n+1):
        m = m*i
    break
print('factorial of',(n) ,'is: ', m)