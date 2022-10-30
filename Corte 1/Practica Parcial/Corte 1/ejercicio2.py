def get_divisores(number):
  sum=0
  for x in range(1, number):
    if number%x==0:
      sum+=x
  return sum

      

def son_panas(number_given):
  pana_counter=0
  for x in range(1,number_given):
    suma=get_divisores(x)
    for y in range(2,number_given):
      if y!=x:
        if suma==y:
          suma2=get_divisores(y)
          if suma2==x:
            pana_counter+=1
        
  return pana_counter









def main():
  number_given=int(input('Please enter a number: \n >>> '))
  print('The number of pana numbers is {}'.format(son_panas(number_given)))


main()