
run='yes'
ans=input('Please enter your first number: \n >>> ')
while not ans.isnumeric:
    num=input('Invalid input. \n >>> ')
ans=int(ans)
while run == "yes":
    operation=input('Please enter the operation you wish to do: \n 1. Sum \n 2. Substraction \n 3. Multiplication \n 4. Divison \n 5. Power \n >>> ')
    while not operation.isnumeric():
        operation=input('Please enter a valid option: \n 1. Sum \n 2. Substraction \n 3. Multiplication \n 4. Divison \n 5. Power \n >>> ')
    operation=int(operation)
    if operation==1:
        num=input("Enter a number: \n >>> ")
        while not num.isnumeric:
            num=input('Invalid input. \n >>> ')
        num=int(num)
        ans+=num
    if operation==2:
        num=input("Enter a number: \n >>> ")
        while not num.isnumeric:
            num=input('Invalid input. \n >>> ')
        num=int(num)
        ans-=num
    if operation==3:
        num=input("Enter a number: \n >>> ")
        while not num.isnumeric:
            num=input('Invalid input. \n >>> ')
        num=int(num)
        ans*=num
    if operation==4:
        num=input("Enter a number: \n >>> ")
        while not num.isnumeric:
            num=input('Invalid input. \n >>> ')
        num=int(num)
        ans/=num
    if operation==5:
        num=input("Enter a number: \n >>> ")
        while not num.isnumeric:
            num=input('Invalid input. \n >>> ')
        num=int(num)
        ans=ans**num
    run=input('Would you like to keep operating? \n Answer "yes" or "no" \n >>> ')
print('Result: {}'. format(ans))