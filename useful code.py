def print_menu():
  print('\nWELCOME TO THE SYSTEM \n What would you like to do?')
  option=input('1. See inventory \n2. Purchase \n 3. Quit \n >>> ')
  while not option.isnumeric() or not option in ['1','2','3']:
    option=input('INVALID INPUT \n \n Please enter a valid option\n1. See inventory \n2. Purchase \n 3. Quit\n >>> ')
  return int(option)


def validate_name():
  student_name=input('Please enter your name: \n >>> ')
  student=student_name.split()
  check_student=''
  for x in student:
    check_student+=x
  while not check_student.isalpha():
       student_name=input('INVALID INPUT \n Please enter your name: \n >>> ')
       check_student=''
       student=student_name.split()
       for x in student:
          check_student+=x
  return student_name

def validate_number(required):
  student_id=input('Please enter your {}: \n >>> '.format(required))
  while not student_id.isnumeric():
    student_id=input('INVALID INPUT \n Please enter your {}: \n >>> '.format(required))
  return int(student_id)

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