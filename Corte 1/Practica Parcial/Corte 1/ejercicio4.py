def is_narcisist(number):
  digits=[int(x) for x in number]
  number=int(number)
  suma=0
  for x in digits:
    suma+=x**len(digits)
  if suma==number:
    is_narcisist=True
  else: 
    is_narcisist=False
  return is_narcisist

def main():
  number=input('Please enter a number: \n >>> ')
  while not number.isnumeric():
    number=input('INVALID INPUT \n  \n Please enter a number: \n >>> ')
  result=is_narcisist(number)
  if result:
    print('The number {} is narcisist'.format(number))
  else:
    print('The number {} is not narcisist'.format(number))


main()