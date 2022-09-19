num=input('Please enter a number: ')
if num.isnumeric():
    num=int(num)
    if num%2==0:
        print(f"{num} is an even number")
    else: 
        print(f"{num} is an odd number")
else:
    print('ERROR. input is not a number')