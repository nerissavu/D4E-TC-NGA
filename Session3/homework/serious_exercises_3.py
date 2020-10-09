import random
word = 'champion'
shuffled = list(word)
random.shuffle(shuffled)
shuffled = ' '.join(shuffled)
print(shuffled) 
answer = input('Your answer: ')
if answer == 'champion':
    print('hurray')
else:
    print('oops')



