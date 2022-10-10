def print_welcome():
  print('Bienvenido al sistema')

def get_option(studies):
  for keys, values in studies.items():
    print('OPCION {}'.format(keys))
    for info, data in values.items():
      print('{}: {}'.format(info,data))
  return input('Por favor ingrese la opcion que desea obtener: \n>>> ')

def get_info(option, clients):
  client_data={'ID': input('Por favor ingrese su numero de cedula \n >>> '),'age': int(input('Por favor ingrese su edad\n >>> ')), 'sex':input('Por favor introduzca su sexo: \n >>> '), 'option': option }
  clients.append(client_data)
  return client_data

def print_receipt(client, option, studies,off):
  print('***** RECIBO *****')
  for keys, values in client.items():
    if keys=='option':
      print('Study: {}'.format(studies[option]['descripcion'].title()))
    else:
      print('Client {}: {}'.format(keys, values))
  print('TOTAL: {}'.format((studies[option]['costo']-off)))

def get_discount(client,studies,option,client_num):
  off=0
  if client['sex']== "F" and client['age']>=55:
    off=studies[option]['costo']*.25
  elif client['sex']== "M" and client['age']>=65:
    off+=studies[option]['costo']*.25
  elif client_num%2!=0:
    off+=studies[option]['costo']*0.02
  return off




def main():
  print_welcome()
  studies={'U':{'descripcion':'ultrasonido', 'costo':8900}, 'T':{'descripcion':'tomografia', 'costo':12640}, 'R':{'descripcion':'Resonancia', 'costo':15600}}
  clients=[]
  option=get_option(studies)
  client=get_info(option, clients)
  discount=get_discount(client,studies,option, len(clients))
  print_receipt(client, option, studies, discount)
  
 

  



main()