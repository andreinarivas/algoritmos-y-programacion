def print_welcome():
  print('\n')
  option=input(('Welcome to the system! What would you like to do? \n 1. Inventory Module \n 2. Purchase Module \n 3. Quit \n>>> '))
  while not option.isnumeric() or not option in ['1','2', '3']:
    print('INVALID INPUT')
    option=input(('Choose valid option \n 1. Inventory Module \n 2. Purchase Module \n 3. Quit \n>>> '))
  return int(option)

def print_inventory(dictionary):
  for id, vinyls in dictionary.items():
    print('\nVINYL #{}'.format(id))
    for info, data in vinyls.items():
      if info=='release_year':
        print('Realease year: {}'.format(data))
      else:
        print('{}: {}'.format(info.capitalize(),data))

def search_vinyl(search_name, dictionary,validate):
  for id,vinyls in dictionary.items():
    for info,data in vinyls.items():
      if info=='name':
        if data.lower()==search_name:
          id_needed=id
          validate=True
          break
  if validate==True:
     print('\n')
     for info, data in dictionary[id_needed].items():
      if info=='release_year':
        print('Realease year: {}'.format(data))
      else:
        print('{}: {}'.format(info.capitalize(),data))
  else:
    print('VINYL NOT FOUND')
  return validate

def get_new_purchase(dictionary):
  new_purchase={}
  dni=input('Please enter the clients ID: \n >>> ')
  while not dni.isnumeric():
    dni=input('INVALID INPUT. \nPlease enter the clients ID: \n >>> ')
  new_purchase['dni']=int(dni)
  new_purchase['name']=input('Please enter the clients name; \n>>> ').title()
  print_inventory(dictionary)
  vinyl_selected=input('Please enter the number of vinyl to purchase: \n >>> ')
  while not vinyl_selected.isnumeric() or not vinyl_selected in ['1','2','3','4','5']:
    vinyl_selected=input('INVALID INPUT\n Please enter the number of vinyl to purchase: \n >>> ')
  new_purchase['vinyl']=dictionary[vinyl_selected]
  #update stock
  dictionary[vinyl_selected]['stock']-=1
  dictionary[vinyl_selected]['sold']+=1
  return new_purchase


def print_receipt(purchases):
  print('\n')
  print('******** RECEIPT *********')
  for info, data in purchases.items():
    if info=='vinyl':
      print('Vinyl Bought: {}'.format(purchases['vinyl']['name']))
      print('Price: {}'.format(purchases['vinyl']['price']))
    else:
      print('{}: {}'.format(info.capitalize(),data))


def main():
  vinyls = {
  '1': { 'name': 'Cuando Los Acéfalos Predominan',
        'author': 'Rawayana',
        'release_year': '2021',
        'stock': 1000,
        'sold': 0,
        'price': 10,
      },
  '2': { 'name': 'Notes on a Conditional Form',
        'author': 'The 1975',
        'release_year': '2020',
        'stock': 1200,
        'sold': 0,
        'price': 20,
      },
  '3': { 'name': 'Call Me If You Get Lost',
        'author': 'Tyler, the Creator',
        'release_year': '2021',
        'stock': 900,
        'sold': 0,
        'price': 30,
      },
  '4': { 'name': 'El Mal Querer',
        'author': 'Rosalía',
        'release_year': '2018',
        'stock': 980,
        'sold': 0,
        'price': 40,
      },
  '5': { 'name': 'The Dark Side of the Moon',
        'author': 'Pink Floyd',
        'release_year': '1973',
        'stock': 500,
        'sold': 0,
        'price': 50,
      },
  }
  purchases={}
  purchase_num=0
  run='yes'
  while run=='yes':
    module_selected=print_welcome()
    if module_selected==1:
      inventory_option=input('Please choose an option: \n 1. See complete inventory \n 2. Search a vinyl  \n>>> ')
      while not inventory_option.isnumeric() or not inventory_option in ['1','2']:
        inventory_option=input('INVALID INPUT \n Please choose an option: \n 1. See complete inventory \n 2. Search a vinyl \n>>> ')
      inventory_option=int(inventory_option)
      if inventory_option==1:
        print_inventory(vinyls)
      if inventory_option==2:
        validate=False
        while validate==False:
          search_name=input('Please enter the name of the vinyl you look for: \n >>> ').lower()
          validate=search_vinyl(search_name, vinyls,validate)
    if module_selected==2:
      purchase_option=input('Please choose an option: \n 1. Register new purchase \n 2. See purchases \n>>> ')
      while not purchase_option.isnumeric() or not purchase_option in ['1','2']:
        purchase_option=input('INVALID INPUT \n Please choose an option: \n 1. Register new purchase \n 2. See purchases \n>>> ')
      purchase_option=int(purchase_option)
      if purchase_option==1:
        purchase_num+=1
        new_purchase=get_new_purchase(vinyls)
        purchases[purchase_num]=new_purchase
        print_receipt(new_purchase)
      if purchase_option==2:
        print('Total Number of Purchases: {}'.format(purchase_num))
        see_more=input('Want to see the details of all purchases? \n Yes (Y) or No (N)\n >>> ')
        while not see_more in ['Y',"N"]:
          see_more=input('INVALID INPUT \n More details? \n Yes (Y) or No (N)\n >>> ')
        if see_more=='Y':
          for id, vinyls in purchases.items():
            print('\n PURCHASE #{}'.format(id))
            for info, data in vinyls.items():
              if info=='vinyl':
                print('Vinyl Bought: {}'.format(purchases[id]['vinyl']['name']))
              else:
                print('{}: {}'.format(info.capitalize(),data))
    if module_selected==3:
      run='no'
      











        






main()

