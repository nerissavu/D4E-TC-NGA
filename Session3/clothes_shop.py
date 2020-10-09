items =  ['mũ','giày','váy','áo']
print('Our items: ')
for i in range(len(items)):
    print(i+1, items[i])

while True:
    print('To exit our store, please type "EXIT"')
    choice = input('welcome to our shop, what do you want? (C R U D): ')
    choice = choice.upper()

    if choice == 'C':
        c = input('Enter new item: ')
        items.append(c)
        for i in range(len(items)):
            print(i+1, items[i])

    elif choice == 'R':
        for i in range(len(items)):
            print(i+1, items[i])

    elif choice == 'U':
        input_index = int(input('Position you want to updtade: '))
        items[input_index - 1] = input('Enter new stuff: ')
        for i in range(len(items)):
            print(i+1, items[i])

    elif choice == 'D':   
        delete_index = int(input('position you want to delete: '))
        items.pop(delete_index - 1)
        for i in range(len(items)):
            print(i+1, items[i])
        
    elif choice == "EXIT":
        print('Thank you')
        break

    else:
        print('invalid action')


