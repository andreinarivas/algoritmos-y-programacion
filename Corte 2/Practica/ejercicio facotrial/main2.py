#This is one way i though first 

def validate_number():
  number=input('Please enter a number: \n >>> ')
  while not number.isnumeric():
    number=('INVALID INPUT \n Please enter a round positive number: \n >>> ')
  return int(number)

def get_factorial(number, result=1, aux=1):
  if aux<=number:
    result*=aux
    aux+=1
    return get_factorial(number,result, aux)
  else:
    return result

def main():
  number=validate_number()
  result=get_factorial(number)
  print('The factorial of {} is {}' .format(number, result))

main()