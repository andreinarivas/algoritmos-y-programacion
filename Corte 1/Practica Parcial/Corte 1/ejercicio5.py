def print_menu():
  print('\nWELCOME TO SAMAN-LABS \n What would you like to do?')
  option=input('1. See inventory \n2. Purchase \n 3. Quit \n >>> ')
  while not option.isnumeric() or not option in ['1','2','3']:
    option=input('INVALID INPUT \n \n Please enter a valid option\n1. See inventory \n2. Purchase \n 3. Quit\n >>> ')
  return int(option)

def print_inventory(data_base):
  print('******* INVENTORY *******\n')
  for types,category in data_base.items():
    print('    ****{} AVAILABLE****\n'.format(types))
    for specialty, medications in category.items():
      print('      **{} AVAILABLE**\n'.format(specialty))
      for organ, medicationlist in medications.items():
        print('      FOR {}: \n'.format(organ))
        for medicine in medicationlist:
          for info, data in medicine.items():
            print('{}: {}'.format(info.upper(),data))

def get_client_data(medications):
  new_client={}
  new_client['Name']=input('Please enter the clients name: \n>>> ')
  client_id=input('Please enter the clients id: \n >>> ')
  while not client_id.isnumeric():
    client_id=input('INAVLID INPUT \n \nPlease enter the clients id: \n >>> ')
  new_client['ID']=int(client_id)
  selection=client_selection(medications)
  new_client['Medication ID Bought']=selection
  new_client['Medication Name Bought']=get_product_name(selection, medications)
  new_client['Total']=get_total(selection, medications)
  return new_client



def client_selection(data_base):
  print('\n Please select the ID of the medicine you wish to purchase: \n ')
  for types,category in data_base.items():
    for specialty, medications in category.items():
      for organ, medicationlist in medications.items():
        for medicine in medicationlist:
          print('\n')
          for info, data in medicine.items():
            if info=='id'or info=='name':
              print('{}: {}'.format(info.upper(),data))
  selection=input('\n >>> ')
  while not selection.isnumeric() or not int(selection) in range(1,15):
    selection=input('INVALID ID \n Please enter a valid ID: \n >>> ')
  return int(selection)

def get_total(selection, data_base):
  for types,category in data_base.items():
    for specialty, medications in category.items():
      for organ, medicationlist in medications.items():
        for medicine in medicationlist:
          for info, data in medicine.items():
            if info=='id':
              if data==selection:
                total=medicine['price']
  return total

def get_product_name(selection, data_base):
  for types,category in data_base.items():
    for specialty, medications in category.items():
      for organ, medicationlist in medications.items():
        for medicine in medicationlist:
          for info, data in medicine.items():
            if info=='id':
              if data==selection:
                name=medicine['name']
  return name
                
def print_receipt(purchase_info):
  print('\n \n')
  print('******* RECEIPT *******')
  for info, data in purchase_info.items():
    print('{}:   {}'.format(info,data))
    
  print('\n')

  


def main():
  medications = {
          "prescription": {
              "antibiotics": {
                  "skin": [
                      {
                          "id": 1,
                          "name": "Clindamicine",
                          "price": 300
                      },
                      { 
                          "id": 2,
                          "name": "Cefadroxil",
                          "price": 350
                      },
                      {
                          "id": 3,
                          "name": "Amoxicillin",
                          "price": 320
                      }
                  ],
                  "respiratory-system":[
                      {
                          "id": 4,
                          "name": "Citromicine",
                          "price": 380
                      },
                      {
                          "id": 5,
                          "name": "Levofloxacine",
                          "price": 125
                      },
                      {
                          "id": 6,
                          "name": "Azitromicine",
                          "price": 740
                      }
                  ]
              },
              "analgesic": {
                  "anti-inflammatories": [
                      {
                          "id": 7,
                          "name": "HYDROCODONE-IBUPROFEN",
                          "price": 150
                      },
                      {
                          "id": 8,
                          "name": "IBUDONE",
                          "price": 180
                      }
                  ]
              }
          },
          "non-prescription": {
              "analgesic": {
                  "general": [
                      {
                          "id": 9,
                          "name": "Acetaminophen",
                          "price": 15
                      },
                      {
                          "id": 10,
                          "name": "Ibuprofen",
                          "price": 20
                      }
                  ]
              },
              "antihistamine": {
                  "antiallergic": [
                      {
                          "id": 11,
                          "name": "Loratadine",
                          "price": 12
                      },
                      {
                          "id": 12,
                          "name": "Desler M",
                          "price": 8
                      },
                      {
                          "id": 13,
                          "name": "Allegra",
                          "price": 21
                      },
                      {
                          "id": 14,
                          "name": "Fexofenadine",
                          "price": 18
                      }
                  ]
              }
          }
      }
  run=True
  purchase_db={}
  purchase_number=0
  while run:
    option=print_menu()
    if option==1:
      print_inventory(medications)
    if option==2:
      purchase_number+=1
      purchase_db[purchase_number]=get_client_data(medications)
      print_receipt(purchase_db[purchase_number])

    if option==3:
      run=False

  




main()
