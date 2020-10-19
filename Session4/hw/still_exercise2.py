numbers = [1, 6, 8, 1, 2, 1, 6, 5]
n = int(input('Enter a number: '))

if numbers.count(n)>1:
    print( n, 'appears', numbers.count(n), 'times in my list')
else:
    print( n, 'appears', numbers.count(n), 'time in my list')

