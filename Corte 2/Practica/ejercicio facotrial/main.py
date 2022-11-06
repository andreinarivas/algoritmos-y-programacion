#This is the other faster way i thought to do it

def validate_number():
  number=input('Please enter a number: \n >>> ')
  while not number.isnumeric():
    number=('INVALID INPUT \n Please enter a round positive number: \n >>> ')
  return int(number)

def get_factorial(number):
  if number==1:
    return number
  else:
    return number*get_factorial(number-1)


def main():
  number=validate_number()
  result=get_factorial(number)
  print('The factorial of {} is {}' .format(number, result))

main()