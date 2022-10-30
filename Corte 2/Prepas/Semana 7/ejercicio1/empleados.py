class Empleados():
  num_employee=0

  def __init__(self, name:str, last_name:str, pay:int):
    self.name=name
    self.last_name=last_name
    self.email=f'{name.lower()}.{last_name.lower()}@enterprises.com'
    self.pay=pay
    Empleados.num_employee+=1
    

  def get_full_name(self):
    return '{} {}'.format(self.name, self.last_name)


class Developer(Empleados):
  def __init__(self, name, last_name, pay, prog_lang):
    super().__init__(name, last_name, pay)
    self.prog_lang=prog_lang

class Manager(Empleados):
  def __init__(self, name, last_name, pay, developers:list(Empleados)):
    super().__init__(name, last_name, pay)
    if developers is None:
      self.developers=[]
    else:
      self.developers=developers
