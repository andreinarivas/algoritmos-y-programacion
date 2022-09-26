number=input('Please enter a round number: ')
while not number.isnumeric():
    print('Invalid input')
    number=input('Please enter a round number:')
number=int(number)
for x in range(1,number+1):
    print_times=x
    while print_times>=1:
        if print_times==1:
            print(print_times)
        else:
            print(print_times, end=" ")
        print_times-=2