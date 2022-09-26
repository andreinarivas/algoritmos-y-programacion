
number=input('Please enter a round number: ')
while not number.isnumeric:
    number=input("Invalid input.\n Please enter a valid number: ")
number=int(number)
counter=1
divisors=[]
conditions=[]
sum=0
check=0

while counter<=number:
    if number%counter==0:
        divisors.append(counter)
    if number==counter*(counter-1):
        conditions.append('Pronic')
    if number==counter**2:
        conditions.append('Square')
    counter+=1
if len(divisors)>2:
    conditions.append('Composite')
else:
    conditions.append('Prime')

for x in range(len(divisors)-1):
    sum+=divisors[x]
    counter=0
    check=divisors[x]
    while counter<=check:
        if 'Free of squares'in conditions:
            break
        else:
            if check==counter**2:
                break
            else:
                conditions.append('Free of squares')
        counter+=1

if sum==number:
    conditions.append('Perfect')
if sum>number:
    conditions.append('Abundant')
else:
    conditions.append('Deficient')

num_string=str(number)
num_str_inv=(num_string[::-1])
if num_str_inv==num_string:
    conditions.append('Palindrome')
print('The number is: ')
for x in range(len(conditions)):
    if x >=len(conditions)-1:
        print('and ' + conditions[x])
    else:
        print(conditions[x], end=", ")

