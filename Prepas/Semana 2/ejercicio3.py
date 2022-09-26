number=input('Please enter a valid number: ')
dice_1=[1,2,3,4,5,6]
dice_2=[1,2,3,4,5,6]
combinations=[]
while not number.isnumeric():
     print('Invalid input')
     number=input('Please enter a valid number: ')
number=int(number)
while not (number>=2 and number<=12):
    print('Invalid input')
    number=input('Please enter a valid number: ')
counter=0
count=0
while counter<7:
    for x in range(0,len(dice_1)):
        if number==dice_1[count]+ dice_2[x]:
            checker='{}-{}'.format(dice_2[x],dice_1[count])
            if checker in combinations:
                break
            else:
                combinations.append('{}-{}'.format(dice_1[count],dice_2[x]))
            count+=1
    counter+=1
print('The number {} is the sum of rolling: '.format(number))
for x in range(0,len(combinations)):
    print('* {}'.format(combinations[x]))