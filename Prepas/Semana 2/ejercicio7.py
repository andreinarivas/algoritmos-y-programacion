number=input('Please enter a number:')
while not number.isnumeric():
    number=input('Invalid input. Please enter a number: ')
num=number
number=int(number)
counter=0
prime_factors=[]
for x in range(2,number+1):
    while number%x==0:
        prime_factors.append(x)
        number/=x
if len(prime_factors)==2:
    print('The number {} is the result of multiplying {} and {}, which both are prime'.format(num, prime_factors[0], prime_factors[1]))
else:
   print('ERROR')