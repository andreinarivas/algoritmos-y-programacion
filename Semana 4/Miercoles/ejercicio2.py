pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300 	
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800 	
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 	
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto's thyroiditis",
            "price": 900
        }
    ],   
}
run='yes'
patients={}
patient_counter=0
while run=='yes':
  option=input('\n **** MENU **** \n Please choose a valid option:\n 1. Register patient\n 2. Show patients by disease \n 3. Quit program \n >>> ')
  while not option.isnumeric() and not option in ['1','2','3']:
    option=input('INVALID INPUT \n Please choose a valid option:\n 1. Register patient\n 2. Show patients by disease \n 3. Quit program \n >>> ')
  option=int(option)
  if option ==1:
    print('\n **** PATIENT REGISTRATION ****\n')
    patient_counter+=1
    new_patient={'name':"", 'last name': '', 'ID':0}
    for info in new_patient.keys():
      new_patient[info]=input("Please enter the patient's {}: \n>>> ".format(info))
    pathology_id=input("Please enter the pathology's ID: \n >>>")
    while not pathology_id.isnumeric() and not pathology_id in ['1','2','3','4','5','6','7','8']:
      pathology_id=input('INVALID INPUT \n Please enter a valid ID: \n >>> ')
    pathology_id=int(pathology_id)
    new_patient['pathology ID']=pathology_id
    patients[patient_counter]=new_patient
    print('\n******** RECEIPT ********\n')
    total=0
    for info, data in patients[patient_counter].items():
      if info =='pathology ID':
        for system, types in pathologies.items():
          for pathology in types:
            if pathology['id']==data:
              print('{}         {}'.format(pathology['name'],pathology['price']))
              total+=pathology['price']
      else:
       print('{}: {}'.format(info, data))
    print('TOTAL : {}'.format(total))
  if option==2:
    if len(patients)==0:
      print('No patients registered.')
    else:
      to_print=[]
      search=int(input('Please enter pathology ID: \n>>> '))
      for patient_number, patient_info in patients.items():
        check=patient_info['pathology ID']
        if check==search:
          to_print.append(patient_number)
      for x in to_print:
        print('\n')
        for info, data in patients[x].items():
          if info!= 'pathology ID':
            print('{}: {}'.format(info,data))
      if len(to_print)==0:
        print('No patients registered for this pathology')
  if option==3:
    run='no'






