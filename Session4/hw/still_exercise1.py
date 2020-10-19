inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['poket'] =  ['seashell', 'strange','berry','lint']   # CREATE
inventory["backpack"].remove('dagger') #DELETE
inventory['gold'] += 50


print(inventory)

