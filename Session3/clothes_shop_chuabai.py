menu = []
choice = input ('Hello chef, what do you want to do with today menu? (C, R, U, D)')
choice = choice.upper()
if choice == 'C':
    new_item = input('enter new item')
    menu.append(new_item)
    print('our items:')
    for i in range(len(menu))
elif choice == 'R':
