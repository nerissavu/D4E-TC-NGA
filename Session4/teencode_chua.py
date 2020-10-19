dictionary = {
    "hc":"học",
    "any":"anh người iu",
    "hk":"không"
}

while True:
    for key in dictionary:
        print(key, end ="\t")

    print()
    input_key = input('Your code?: ')
    if input_key in dictionary:
        print('It means:', dictionary[input_key])
    else:
        choice = input('Not found your word, wanna contribute? (Y/N)').upper()
        if choice == "Y":
            dictionary[input_key] = input("Enter it meaning: ")
        else:
            print('bye')
            break