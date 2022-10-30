def get_riqueza(matriz):
  max_wealth=0
  for x in matriz:
    if int(sum(x))>max_wealth:
      max_wealth=sum(x)
  return max_wealth

def main():
  matriz=[[1,2,3],[2,2,3]]
  riqueza=get_riqueza(matriz)
  print('MAX WEALTH: {}'.format(riqueza))


main()