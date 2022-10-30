number=input('Please enter a round number: ')
while not number.isnumeric():
    print('Invalid input')
    number=input('Please enter a round number:')
number=int(number)
for x in range(number+1):
    print("*"*x)