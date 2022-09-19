age=(input("Please enter the client's age: "))
if age.isnumeric():
    age=int(age)
    if age<4:
        print('Ticket price: $0.0')
    elif (age>=4 and age<18):
        print('Ticket price: $5.0')
    elif age>=18:
        print('Ticket price: $10.0')
else:
    print('ERROR. input is invalid')