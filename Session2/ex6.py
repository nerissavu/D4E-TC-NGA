user_name = input("user_name: ")
password = input('password:')

switch = True
while switch:
    if user_name == 'ngavu' and password == 'ngavu' :
        print('welcome')
        switch = False
        break
    else: 
        print ('bye')
        user_name = input("user_name: ")
        password = input('password:')





