import random
words = ['rainbow', 'computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 
             'water', 'board', 'geeks'] 
word = random.choice(words)
shuffled = list(word)
random.shuffle(shuffled)
shuffled = ' '.join(shuffled)
print(shuffled) 
answer = input('Your answer: ')
if answer == word:
    print('hurray')
else:
    print('oops')



