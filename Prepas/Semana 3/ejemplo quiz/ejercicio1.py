num=input('Please enter a round number: \n >>> ')
digits=[]
while not num.isnumeric():
  num=input('Invalid input. \n Please enter a round number: \n >>> ')
digits=[int(x) for x in num]
sum=0
is_repunit=True
for x in digits:
  sum+=x
  if x!=digits[0]:
    is_repunit=False
if is_repunit==True:
  print('The number {} is Repunit'.format(num))
else:
  print('The number {} is not Repunit'.format(num))

square=sum**(1/2)
if square/int(square)==1:
  print("The sum of the digits of {}, {}, is a square".format(num, sum))
else:
  print("The sum of the digits of {}, {}, is a not square".format(num, sum))