number=input('Please enter a number: \n>>> ')
while not number.isnumeric:
    number=input("Invalid input.\n Please enter a valid number: ")
number=int(number)
counter=1
while counter<=number:
  if number==counter*(counter-1):
    is_pronic=True
    break
  else:
    is_pronic=False
  counter+=1

if is_pronic==True:
  print('The number {} is pronic'.format(number))
if is_pronic==False:
  print('The number {} is not pronic'.format(number))