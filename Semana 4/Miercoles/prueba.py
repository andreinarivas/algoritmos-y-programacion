search=int(input('Please enter pathology ID'))
possibility=1
patienst={1:{'name':'Luis', 'last name':'Perez', 'ID':758, 'pathology_id':5},2:{'name':'pedro', 'last name':'Perez', 'ID':2675, 'pathology_id':4},3:{'name':'laura', 'last name':'Perez', 'ID':254875, 'pathology_id':5},}
key_x=0
if possibility==1:
  for patient_number, patient_info in patienst.items():
    for data, info in patient_info.items():
      if data=='ID':
        if info==search:
          key_x=patient_number
  patienst.pop(key_x)
  print(patienst)

if possibility==2:
  for patient_number, patient_info in patienst.items():
    if patient_info['ID']==search:
      key_x=patient_number
  patienst.pop(key_x)
  print((patienst))
