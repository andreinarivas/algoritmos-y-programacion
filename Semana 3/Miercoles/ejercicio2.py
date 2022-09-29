information={}
run="yes"
while run=="yes":
    given=input('Please enter what type of information you will introduce: ')
    if not given in information:
        data=input('Please enter the information: \n')
        information[given.capitalize()]=data.capitalize()
        for given, data in information.items():
            print('{}: {}'.format(given, data))
        run=input("\n Would you like to add more information? \n Answer 'yes' or 'no' \n >>> ")
    else:
        print("{} already saved. \n Please introduce new information".format(given.upper()))