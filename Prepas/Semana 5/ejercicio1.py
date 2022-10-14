def get_number():
  while True:
    try: 
      number=int(input('Please enter the number you would like to calculate: \n>>> '))
      if number ==0:
        raise Exception()
      break
    except:
      print('INVALID INPUT.')
  return number

def factorial(number_given):
  sum=1
  for x in range(1, number_given+1):
    sum*=x
  return sum



def main():
  number_given=get_number()
  print('The factorial of {} is {}'. format(number_given, factorial(number_given)))


main()