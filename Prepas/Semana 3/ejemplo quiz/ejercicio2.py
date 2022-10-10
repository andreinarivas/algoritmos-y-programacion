infraction={1:{"name":"Choque", "cost":50}, 2:{"name":"Semáforo", "cost":30}, 3:{"name":"Falta de documentos", "cost":100},}
officers={ 1:{"name":"Luis", "last name":"Bello","ci":13452224}, 2:{"name":"Jose", "last name":"Quevedo","ci":44235611}, 3:{"name":"Antonio", "last name":"Guerra","ci":12345678},}
db={}
infraction_info={}
officers_info={}
number_of_infractions=3
run='yes'
while run=='yes':
  option=input('\nWelcome to the system. What would you like to do today? \n Please enter a valid option. \n 1. Add infraction \n 2. Register payment \n 3. Show existing infractions \n 4. Close program \n >>> ')
  while not option.isnumeric() or not option in ['1','2','3','4']:
    print('ERROR. \n Invalid Input')
    option=input('Please enter a valid option. \n 1. Add infraction \n 2. Register payment \n 3. Show existing infractions \n 4. Close Program \n >>> ')
  option=int(option)
  if option==1:
    print('ADD INFRANCTION')
    is_unique='no'
    name_of_infraction=input('Please enter the name of the infraction: \n >>> ')
    while is_unique=='no':
      for x in infraction.keys():
        value=infraction[x]['name']
        if value==name_of_infraction.capitalize():
          name_of_infraction=input('Infraction already existis. \nPlease enter a different name for the infraction: \n >>> ').capitalize()
        else:
          is_unique='yes'
    cost_of_infraction=input('Please enter the cost of the infraction: \n >>> ')
    while not cost_of_infraction.isnumeric():
      cost_of_infraction=input('Invalid input. \n Please enter the cost of the infraction: \n >>> ')
    cost_of_infraction=int(cost_of_infraction)
    number_of_infractions+=1
    infraction_info['name']=name_of_infraction
    infraction_info['cost']=cost_of_infraction
    infraction[number_of_infractions]=infraction_info
    name_of_officer=input('Please enter the name of the officer that registered the infraction: \n >>> ').capitalize()
    l_name_of_officer=input('Please enter the last name of the officer that registered the infraction: \n >>> ').capitalize()
    ci_of_officer=input("Please enter the officer's ID: \n >>>")
    while not ci_of_officer.isnumeric():
      ci_of_officer=input("Invalid Input. \n Please enter the officer's ID: \n >>>")
    ci_of_officer=int(ci_of_officer)
    officers_info['name']=name_of_officer
    officers_info['last name']=l_name_of_officer
    officers_info['ci']=ci_of_officer
    officers[number_of_infractions]=officers_info
    print('Registration Successful')
  if option==2:
    print('PAYMENT REGISTRATION')
    key_needed=0
    while key_needed==0:
      search_key=input('Please enter a valid name for infraction: \n >>> ')
      for x in infraction.keys():
        value=infraction[x]['name']
        if value==search_key.capitalize():
          key_needed=x
          break
      else:
        print('Infraction does not exist.')
    print('The cost of the infraction "{}" is {} dollars'.format(infraction[key_needed]['name'],infraction[key_needed]['cost']))
    payment=input('Please enter the amount payed: \n >>> ')
    while not payment.isnumeric():
      payment=input("Invalid Input. \n Please enter the amount payed: \n >>>")
    payment=int(payment)
    if payment>=infraction[key_needed]['cost']:
      infraction.pop(key_needed)
      officers.pop(key_needed)
      print('Infraction fully payed. \n It has been succesfully eliminated from system.')
    else:
      infraction[key_needed]['cost']-=payment
      print('Infraction partially payed. \n Remaining debt: ${} \n Infraction must be fully payed to be eliminated from system'.format(infraction[key_needed]['cost']))
  if option==3:
    print('INFRACTIONS REGISTERED')
    for x in infraction.keys():
      print('\nInfraction #{}'.format(x))
      for info, data in infraction[x].items():
        print('{} of infraction: {}'.format(info.capitalize(), data))
      for info, data in officers[x].items():
        print('{} of officer who registered: {}'.format(info.capitalize(), data))
  if option==4:
    print('Thank you for using this service. \nHave a nice day!')
    run='no'