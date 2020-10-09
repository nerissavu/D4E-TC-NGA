def print_menu():
    print('our items: ')
        for i in range(len(menu)):
            print(f'{i+1}.{menu[i]}')

menu = ['phở','cơm','bún','thịt chó','bún đậu']

while True:
    choice = input ('Hello chef, what do you want to do with today menu? (C, R, U, D): ')
    choice = choice.upper()
    if choice == 'C':
        new_item = input('Enter new item: ')
        menu.append(new_item)
        print_menu()
    elif choice == 'R':
        print('our items: ')
        for i in range(len(menu)):
            print(f'{i+1}.{menu[i]}')
    elif choice == 'U':
        index = int(input('Enter update position: ')) - 1
        menu[index] = input('Enter new value: ')
        print_menu()
    elif choice == 'D': 
        index = int(input('Enter delete position')) - 1
        menu.pop(index)
        print_menu()
    else:
        print('invalid action')
        break