number=int(input('Please enter a round number: '))
for x in range(1,number+1):
    if x%2!=0:
        if x >=number-1:
            print(x)
        else:
            print(x, end=",")



