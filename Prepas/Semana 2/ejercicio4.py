number=input('Please enter a round number: ')
while not number.isnumeric():
    print('Invalid output')
    number=input('Please enter a valid number: ')
number=int(number)
initial_x=0
second_x=1
sum=0
total_sums=[0,1]
while sum<number:
    sum=initial_x+second_x
    initial_x=second_x
    second_x=sum
    total_sums.append(sum)
print(total_sums)

