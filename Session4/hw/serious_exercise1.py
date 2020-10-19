name = str(input('Write your name: '))

name_lower = name.lower()
name_notab = " ".join(name_lower.split())
updated_name = name_notab.title()

print('Updated:', updated_name)