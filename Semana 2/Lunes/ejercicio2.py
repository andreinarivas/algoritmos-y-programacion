
name=input('Please enter your full name: ')
if not name.isnumeric():
    print(name.lower())
    print(name.upper())
    print(name.title())
else:
    print('EROOR. input is ivalid')