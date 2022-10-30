def print_welcome():
  print('Welcome to the system! \n Select an option:')
  module_option= input('\n A. Administrator \n U. User \n Q. Quit \n >>> ')
  while not module_option in ['A','U', 'Q']:
    module_option=input('INVALID INPUT. Please enter a valid option \n A. Administartor \n U. User \n Q. Quit \n >>> ')
  
  return module_option

def get_total(shipment_options, new_shipment):
  total=0
  extra=0
  total+=new_shipment['Package Weight']*shipment_options[new_shipment['Shipment Type']]['price']
  total+=shipment_options[new_shipment['Shipment Type']]['service']
  if new_shipment['Repackaging']=='Y':
    extra+=total*0.03
  if new_shipment['Insurance']=='Y':
    extra+=total*0.01
  total+=extra
  return total


def register_deliver(shipment_options,payments_methods):
  new_shipment={}
  client_id=input('Please enter your id: \n >>>')
  while not client_id.isnumeric():
    client_id=input('INVALID INPUT\n. Please enter your id: \n >>>')
  new_shipment['Client ID']=int(client_id)
  new_shipment['Client Name']=input('Please enter your name: \n >>> ')
  for id, option in shipment_options.items():
    print('OPTION {}'.format(id))
    for info, data in option.items():
      print('{}: {}'.format(info.capitalize(),data))
  shipment_selected=input('Please enter the number of option for shipment: \n>>>')
  while not shipment_selected.isnumeric() or not shipment_selected in ['1','2']:
    shipment_selected=input('INVALID INPUT. \n Please enter the number of option for shipment: \n>>>')
  new_shipment['Shipment Type']=int(shipment_selected)
  payment_method=input('Please enter the payment method preferred: \n 1. Zelle \n 2. Cash \n 3. Credit or Debit Card \n >>>')
  while not payment_method.isnumeric() or not payment_method in ['1','2','3']:
    payment_method=input('INVALID INPUT \n Please enter the payment method preferred: \n 1. Zelle \n 2. Cash \n 3. Credit or Debit Card \n >>>')
  new_shipment['Payment Method']=payments_methods[int(payment_method)]
  weight=input('Please enter the weight of your package: \n >>> ')
  while not weight.isnumeric():
     weight=input('INVALID INPUT. \nPlease enter the weight of your package: \n >>> ')
  weight=int(weight)
  new_shipment['Package Weight']=weight
  reembalaje=input('Please select if you want repackaging: \n Yes (Y) or No (N) \n >>>')
  while not reembalaje in ['Y', 'N']:
    reembalaje=input('INVALID INPUT \n Please select if you want repackaging: \n Yes (Y) or No (N) \n >>>')
  new_shipment['Repackaging']=reembalaje
  insurance=input('Please select if you want insurance: \n Yes (Y) or No (N) \n >>>')
  while not insurance in ['Y', 'N']:
    insurance=input('INVALID INPUT \n Please select if you want insurance: \n Yes (Y) or No (N) \n >>>')
  new_shipment['Insurance']=insurance
  new_shipment['Total price']=get_total(shipment_options, new_shipment)
  print_receipt(new_shipment)
  return new_shipment

def print_receipt(new_shipment):
  print('******* RECEIPT *******')
  for info, data in new_shipment.items():
    print('{}: {}'.format(info.capitalize(),data))

def get_data(new_shipment):
  number_of_ship=0
  total_of_ship=0
  number_of_plane=0
  total_of_plane=0
  for id, shipment in new_shipment.items():
    for info, data in shipment.items():
      if info=='Shipment Type':
        if data==1:
          number_of_ship+=1
          total_of_ship+=shipment['Total price']
        if data==2:
          number_of_plane+=1
          total_of_plane+=shipment['Total price']
  print('The number of ship shipments: {}'.format(number_of_ship))
  print('The number of plane shipments: {}'.format(number_of_plane))
  print('Total price of ship shipments: {}'.format(total_of_ship))
  print('Total price of plane shipments: {}'.format(total_of_plane))

def search_client(data_base):
  client_wanted= input('Please enter the id of the client: \n >>>')
  while not client_wanted.isnumeric():
    client_wanted=input('INVALID INPUT. Please enter the id of the client: \n >>>')
  client_wanted=int(client_wanted)
  client_w_id=0
  found='no'
  for id, shipment in data_base.items():
    if client_wanted==data_base[id]['Client ID']:
      client_w_id=id
      found='yes'
  if found=='yes':
    print('Order #{}'.format(client_w_id))
    print('Order from {}'.format(client_wanted))
    for info,data in data_base[client_w_id].items():
      print('{}: {}'.format(info,data))
  else:
    print('NO CLIENT FOUND')
      
  



def main():
  data_base={}
  shipment_number=0
  shipment_options={1:{'type':'Sea', 'price':2, 'service': 10}, 2:{'type':'Areal', 'price':4, 'service':15}}
  payments_methods={1: 'Zelle', 2: 'Cash', 3:'Card'}
  run=True
  while run==True:
    module_selected=print_welcome()
    if module_selected=='U':
      shipment_number+=1
      data_base[shipment_number]=register_deliver(shipment_options, payments_methods)
    if module_selected=='A':
      administration_options=input('Please select what you would like to do: \n 1. See sumary of shipments \n 2. Search shipment by client dni\n>>> ')
      while not administration_options.isnumeric() or not administration_options in ['1','2']:
        administration_options=input('INVALID INPUT \n Please select what you would like to do: \n 1. See sumary of shipments \n 2. Search shipment by client dni\n>>> ')
      administration_options=int(administration_options)
      if administration_options==1:
        get_data(data_base)
      if administration_options==2:
        search_client(data_base)
    if module_selected=='Q':
      run=False


      






main()