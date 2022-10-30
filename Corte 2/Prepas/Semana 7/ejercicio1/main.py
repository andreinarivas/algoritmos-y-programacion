from empleados import Empleados

def main():
  add=True
  empleados=[]
  while add:
    new_employee=None
    name=input('Please enter the name of the employee: \n >>> ')
    last_name=input('Please enter the last name of the employee: \n >>> ')
    pay=input('Please enter the pay of the employee: \n >>> ')
    new_employee=Empleados(name, last_name, pay)
    empleados.append(new_employee)
    add=input('Do you want to add more employees? \n Yes (Y) or No (N )>>> ')
    if add=='N':
      add=False
  for x in empleados:
    print('\n')
    print(x.get_full_name())
    print(x.email)
    print(x.get_number_employee())
    
  for x in empleados:
    for y, z in x.__dict__.items():
      print('{}: {}'.format(y,z))



main()