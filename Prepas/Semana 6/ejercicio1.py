
def get_client_wealth(accounts):
  more_clients=True
  while more_clients:
    more_accounts=True
    new_clients=[]
    while more_accounts:
      account_wealth=input('Please enter the amount of money in an account: \n >>> ')
      while not account_wealth.isnumeric():
        account_wealth=input('INVALID INPUT \nPlease enter the amount of money in an account: \n >>> ')
      new_clients.append(int(account_wealth))
      more_accounts=input('\n Do you want to add more accounts: \n Yes(Y) or No (N) \n >>> ')
      if more_accounts=='N':
        more_accounts=False
    accounts.append(new_clients)
    more_clients=input('\n Do you want to add more clients: \n Yes(Y) or No(N) \n >>> ')
    if more_clients=='N':
      more_clients=False

def calculator(accounts:list(list(int()))):
  max_wealth=0
  index_max=0
  answer=[]
  for x in accounts:
    total_sum=0
    for y in x:
      total_sum+=y
    if total_sum>max_wealth:
      max_wealth=total_sum
      index_max=accounts.index(x)
  answer.append(max_wealth)
  answer.append(index_max)
  return answer



def main():

  accounts= []
  get_client_wealth(accounts)
  result=calculator(accounts)
  print('The maximum amount of wealth is {}, of client #{}'.format(result[0], result[1]+1))

main()
