
teencode = {
    "hc": "Học", 
    "ng": "Người", 
    "pt": "Phốt",
    "ns": "Nói",
    "lm": "Làm",
    "stt": "Số thứ tự",
}

while True:
    print('______________________________________')
    for key in teencode:
        print(key, end ='\t')
    print()
    code = input("Your code?")

    if code == key:
        print('trans:',teencode[key])
    else:
        choice = input('not found, do you want to contribute this word? (Y/N)?')
        choice = choice.upper()

        if choice == "N":
            print('Thank you')
            break

        elif choice == "Y":
            new_code = input('Enter your trans: ')
            teencode[code] = new_code   # CREATE
            print('UPDATED')

        else:
            print('invalid action')
                
                