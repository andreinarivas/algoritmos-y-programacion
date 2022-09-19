num1=(input('Please enter first number: '))
num2=(input('Please enter second number: '))
if num1.isnumeric()and num2.isnumeric():
    num1=float(num1)
    num2=float(num2)
    if num2==0:
        print('ERROR. division is undefined')
    else:
        division=num1/num2
        print(f'The answer is {division}')
else:
    print("ERROR. input is invalid. please restart" )