from person import Person, Redactor, Boss

def main():
  add=True
  writers=[]
  while add:
    name=input('Please enter the name of the employee: \n >>> ')
    identification=input('Please enter the last name of the employee: \n >>> ')
    section=input('Please enter the pay of the employee: \n >>> ')
    new_employee=Redactor(name, identification, section)
    writers.append(new_employee)
    add=input('Do you want to add more employees? \n Yes (Y) or No (N )>>> ')
    if add=='N':
      add=False
  manager=Boss('Pedro', 29551884, 'Sports', writers)
  print(manager.writers[0].name)

main()